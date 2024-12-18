from utils.database import Database
from classes.subquestion import Subquestion
from classes.chunk import Chunk
from langchain_core.documents import Document
import time
import re
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from utils.logger import logChunks, logRankedChunks, logQuery
from utils.promt_templates import RERANKING_PROMPT, HyDE_PROMPT


class retrieval_agent:

    def __init__(self, config: dict, database: Database):

        self.config = config
        self.database = database
        self.llm = AzureChatOpenAI(
            api_version=config["retrieval"]["reranking"]["api-version"],
            deployment_name=config["retrieval"]["reranking"]["model"],
            model_name=config["retrieval"]["reranking"]["model"],
            temperature=config["retrieval"]["reranking"]["temperature"],
        )

    def retrieveChunksForSubquestion(self, subquestion: Subquestion) -> list[Chunk]:

        # Get chunks from the retrieval model
        query = self._createQuery(subquestion, self.config["retrieval"]["vectorSearch"]["useHydeQuery"])
        odata_filter = self._createFilter(subquestion)
        logQuery(query)

        # Create filters for law and commentary documents
        law_document_filter = "(Category eq 'Law' or Category eq 'Ordinance')" + (f" and {odata_filter}" if odata_filter != "" else "")
        commentary_document_filter = "(Category eq 'Published Practice' or Category eq 'Commentary')" + (f" and {odata_filter}" if odata_filter != "" else "")

        # Query for both law and commentary documents and merge them afterwards (ensures that we get a good mix of both)
        law_retrieved_documents = self.database.getRelevantDocuments(
            query,
            top=self.config["retrieval"]["vectorSearch"]["seedChunks"] // 2,
            odata_filter=law_document_filter,
            search_type=self.config["retrieval"]["vectorSearch"]["searchType"]
        )
        commentary_retrieved_documents = self.database.getRelevantDocuments(
            query,
            top=self.config["retrieval"]["vectorSearch"]["seedChunks"] // 2,
            odata_filter=commentary_document_filter,
            search_type=self.config["retrieval"]["vectorSearch"]["searchType"]
        )
        retrieved_documents = law_retrieved_documents + commentary_retrieved_documents

        # Expand the chunks
        expanded_chunks = []

        for document in retrieved_documents:
            chunk = self._expandChunk(document, subquestion.id, min_characters=self.config["retrieval"]["chunkProcessing"]["chunkMinExpansion"])
            expanded_chunks.append(chunk)
        logChunks(f"Retrieved Expanded Chunks ({len(expanded_chunks)})", expanded_chunks)

        cleaned_chunks = self._cleanChunks(expanded_chunks)  # TODO: Check if cleaned chunks are overlapping
        logChunks(f"Cleaned Chunks ({len(cleaned_chunks)})", cleaned_chunks)

        # Rerank the chunks and sort them by score
        reranked_and_sorted_chunks = self._rerankChunks(cleaned_chunks, subquestion)
        logRankedChunks(reranked_and_sorted_chunks, self.config["retrieval"]["vectorSearch"]["outputChunks"])

        # Return the first 'number_of_output_chunks' chunks
        return reranked_and_sorted_chunks[:self.config["retrieval"]["vectorSearch"]["outputChunks"]]


    ####################################################################################################
    #
    #    Private methods
    #
    ####################################################################################################

    def _createFilter(self, subquestion: Subquestion) -> str:

        odata_filter = ""

        # Add the filters to the odata filter
        for i, (key, value) in enumerate(subquestion.filters.items()):
            if i == 0:
                odata_filter += f"{key} eq '{value}'"
            else:
                odata_filter += f" and {key} eq '{value}'"

        return odata_filter

    def _createQuery(self, subquestion: Subquestion, use_hyde: bool) -> str:

        query = subquestion.question

        # TODO: Maybe we can seperate query and hyde query and search the database for them one by one

        if use_hyde:
            #query = subquestion.question  # TODO: Implement the hyde query

            hyde_query_chain = self._get_hyde_query_chain()
            hyde_query = hyde_query_chain.invoke({"question": query})

            query = query + "\n\n" + hyde_query
            query = query.strip()

        return query

    def _expandChunk(self, document: Document, subquestion_id: int, min_characters: int = 1500) -> Chunk:

        group = [document]
        content = document.page_content

        # Initialize the previous and next document
        prev_doc = document
        next_doc = document

        while (len(content) < min_characters) and (prev_doc is not None or next_doc is not None):

            # Get the previous and next document
            prev_doc = self.database.getDocumentById(prev_doc.metadata.get("prev")) if prev_doc is not None else None
            next_doc = self.database.getDocumentById(next_doc.metadata.get("next")) if next_doc is not None else None

            # Add them to the group if they exist and update the content
            if prev_doc is not None:
                assert prev_doc not in group, f"Document {prev_doc.metadata.get('key')} already in group --> loop detected"

                group.insert(0, prev_doc)
                content = prev_doc.page_content + content

            if next_doc is not None:
                assert next_doc not in group, f"Document {next_doc.metadata.get('key')} already in group --> loop detected"

                group.append(next_doc)
                content = content + next_doc.page_content

        return Chunk(content, 0, document.metadata.get("source"), subquestion_id, group)

    def _rerankChunks(self, chunks: list[Chunk], subquestion: Subquestion) -> list[Chunk]:

        # Calculate a score for each chunk
        for chunk in chunks:
            reranking_chain = self._get_reranking_chain()
            raw_ranking = reranking_chain.invoke({"case": subquestion.question, "chunk": chunk.data})
            #print(f"Raw ranking for chunk for subquestion {subquestion.id}: {raw_ranking}")

            score_match = re.search(r"Score:\s*(\d+)", raw_ranking)
            score = int(score_match.group(1)) if score_match else -1   # -1 if no score found
            chunk.ranking_score = score
            time.sleep(1)

        # Sort the chunks by ranking score
        sorted_chunks = sorted(chunks, key=lambda x: x.ranking_score, reverse=True)
        return sorted_chunks
    
    def _cleanChunks(self, expanded_chunks: list[Chunk]) -> list[Chunk]:
        # Clean the chunk by combining the overlapping chunks

        def has_overlap(chunk1: Chunk, chunk2: Chunk) -> bool:
            # Check if two chunks overlap, we do so by checking the keys of the documents in the chunks
            keys1 = [doc.metadata.get("key") for doc in chunk1.documents]
            keys2 = [doc.metadata.get("key") for doc in chunk2.documents]
            keys1_set = set(keys1)
            keys2_set = set(keys2)
            return not keys1_set.isdisjoint(keys2_set)

        #cleaned_chunks = expanded_chunks  # TODO: Check for overlaps and merge chunks if necessary
        cleaned_chunks = []
        for chunk in expanded_chunks:
            # For each chunk in the expanded_chunks, check if it overlaps with any of the cleaned_chunks
            # If it does, merge the two chunks
            # If it does not, add the chunk to the cleaned_chunks
            overlap = False
            for cleaned_chunk in cleaned_chunks:
                if has_overlap(chunk, cleaned_chunk):
                    overlap = True

                    chunk_keys = [doc.metadata.get("key") for doc in chunk.documents]
                    cleaned_chunk_keys = [doc.metadata.get("key") for doc in cleaned_chunk.documents]

                    # Show the number of keys overlapping
                    print(f"Number of keys overlapping: {len(set(chunk_keys).intersection(set(cleaned_chunk_keys)))}")

                    print(f"Chunk keys: {chunk_keys}")
                    print(f"Cleaned chunk keys: {cleaned_chunk_keys}")

                    # Merge the chunk into the cleaned_chunk. We do so by adding the documents of the chunk to the cleaned_chunk
                    # Here we need to preserve the order of the documents in both chunks
                    # If the first document of the chunk is not in the cleaned_chunk, we add the documents of the chunk to the cleaned_chunk starting from the beginning and stopping when we find a document that is already in the cleaned_chunk
                    # Repeat the same for the last document of the chunk from the end

                    chunk_keys = [doc.metadata.get("key") for doc in chunk.documents]
                    cleaned_chunk_keys = [doc.metadata.get("key") for doc in cleaned_chunk.documents]

                    # len_chunk = len(chunk.documents)
                    # if chunk.documents[0] not in cleaned_chunk.documents:
                    #     for i in range(len_chunk):
                    #         if chunk.documents[i] in cleaned_chunk.documents:
                    #             break
                    #         cleaned_chunk.documents.insert(i, chunk.documents[i])
                    # if chunk.documents[-1] not in cleaned_chunk.documents:
                    #     new_ones = []
                    #     for i in range(len_chunk - 1, -1, -1):
                    #         if chunk.documents[i] in cleaned_chunk.documents:
                    #             break
                    #         new_ones.append(chunk.documents[i])
                    #     cleaned_chunk.documents += new_ones[::-1]

                    len_chunk = len(chunk.documents)
                    if chunk_keys[0] not in cleaned_chunk_keys:
                        for i in range(len_chunk):
                            if chunk_keys[i] in cleaned_chunk_keys:
                                break
                            cleaned_chunk.documents.insert(i, chunk.documents[i])
                    if chunk_keys[-1] not in cleaned_chunk_keys:
                        new_ones = []
                        for i in range(len_chunk - 1, -1, -1):
                            if chunk_keys[i] in cleaned_chunk_keys:
                                break
                            new_ones.append(chunk.documents[i])
                        cleaned_chunk.documents += new_ones[::-1]
                    
            # TODO: Check if cleaned chunks are overlapping

            if not overlap:
                cleaned_chunks.append(chunk)

        # Make sure that all the documents in expanded_chunks are in cleaned_chunks
        expanded_chunks_documents_keys = []
        for chunk in expanded_chunks:
            expanded_chunks_documents_keys.extend([doc.metadata.get("key") for doc in chunk.documents])
        cleaned_chunks_documents_keys = []
        for chunk in cleaned_chunks:
            cleaned_chunks_documents_keys.extend([doc.metadata.get("key") for doc in chunk.documents])
        
        # Assert that all the documents in expanded_chunks are in cleaned_chunks and return the number of documents in each
        assert len(set(expanded_chunks_documents_keys)) == len(set(cleaned_chunks_documents_keys)), f"Number of documents in expanded_chunks: {len(expanded_chunks_documents_keys)}, Number of documents in cleaned_chunks: {len(cleaned_chunks_documents_keys)}"

        # Recreate the data of the cleaned chunks
        for chunk in cleaned_chunks:
            chunk.data = ""

            # Make sure that the documents are not repeated
            chuck_documents_keys = [doc.metadata.get("key") for doc in chunk.documents]
            assert len(set(chuck_documents_keys)) == len(chuck_documents_keys), f"Documents repeated in chunk: {chuck_documents_keys}"

            for doc in chunk.documents:
                chunk.data += doc.page_content

        return cleaned_chunks

    def _get_reranking_chain(self):

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", RERANKING_PROMPT),
                ("human", "Case: {case},  Document: {chunk}"),
            ]
        )

        return prompt | self.llm | StrOutputParser()

    def _get_hyde_query_chain(self):

        prompt = ChatPromptTemplate.from_template(HyDE_PROMPT)

        return prompt | self.llm | StrOutputParser()


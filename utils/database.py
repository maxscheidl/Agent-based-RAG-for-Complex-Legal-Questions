from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores.azuresearch import AzureSearch
from langchain_core.documents import Document

from utils.localDocumentDatabase import LocalDocumentDatabase
import os

class Database:

    def __init__(self):

        # Instantiate embeddings for the search
        self.embeddings = AzureOpenAIEmbeddings(
            azure_deployment="text-embedding-3-large"
        )

        # Instantiate the AzureSearch object for vector search
        self.grouped_vector_store = AzureSearch(
            azure_search_endpoint=os.environ.get("AZURE_SEARCH_ENDPOINT"),
            azure_search_key=os.environ.get("AZURE_SEARCH_API_KEY"),
            index_name="tax-docs-emmbeddings-3",
            semantic_configuration_name="default",
            embedding_function=self.embeddings.embed_query,
        )

        # Local database to retrieve documents by their key
        self.localDatabase = LocalDocumentDatabase()

    def getRelevantDocuments(self, query: str, top: int = 10, odata_filter: str = "", search_type: str = "similarity"):

        match search_type:
            case "similarity":
                retrieved_documents = self.grouped_vector_store.vector_search(query, k=top, filters=odata_filter)
            case "hybrid":
                retrieved_documents = self.grouped_vector_store.hybrid_search(query, k=top, filters=odata_filter)
            case "semantic_hybrid":
                retrieved_documents = self.grouped_vector_store.semantic_hybrid_search(query, k=top, filters=odata_filter)
            case _:
                raise ValueError(f"search_type of {search_type} not allowed.")

        return retrieved_documents

    def getDocumentById(self, doc_id: str) -> Document:
        return self.localDatabase.get_document_by_id(doc_id)

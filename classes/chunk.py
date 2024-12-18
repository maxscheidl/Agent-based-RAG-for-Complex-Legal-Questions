from langchain_core.documents import Document


class Chunk:

    def __init__(self, data: str, confidence_score: float, provenance: str, subquestion_id: int, original_documents: list[Document]):

        self.data = data
        self.ranking_score = 0
        self.confidence_score = confidence_score
        self.provenance = provenance
        self.subquestion_id = subquestion_id
        self.documents = original_documents

    def __str__(self):
        return f"Chunk: Documents: {len(self.documents)} (Confidence: {self.confidence_score}): Provenance: {self.provenance}, Subquestion ID: {self.subquestion_id}"


import json
import sqlite3
import os
from langchain_core.documents import Document


class LocalDocumentDatabase:

    def __init__(self, db_name="tax_documents.db", table_name="documents"):
        self.db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', db_name)
        self.table_name = table_name
        self.init_db()

    def init_db(self):

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id TEXT PRIMARY KEY,
                content TEXT,
                metadata TEXT,
                prev_id TEXT,
                next_id TEXT,
                FOREIGN KEY(prev_id) REFERENCES {self.table_name}(id),
                FOREIGN KEY(next_id) REFERENCES {self.table_name}(id)
            )
            """
            )

        conn.commit()
        conn.close()

    def get_document_by_id(self, doc_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute(f"""SELECT id, content, metadata, prev_id, next_id FROM {self.table_name} WHERE id=?""", (doc_id,) , )

        row = cursor.fetchone()
        conn.close()

        if row:
            doc_id, content, metadata, prev_id, next_id = row
            metadata = json.loads(metadata)
            return Document(page_content=content, metadata=metadata)

        # if none is found return none
        return None


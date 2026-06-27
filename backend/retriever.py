import os

from backend.vector_store import VectorStoreManager


class DocumentRetriever:
    """
    Retrieves the most relevant document chunks from a selected FAISS index.
    """

    def __init__(self):
        self.vector_manager = VectorStoreManager()

    def retrieve(self, query, document_name, k=4):
        """
        Retrieve top-k relevant chunks from the selected document.
        """

        vector_path = os.path.join(
            "vectorstore",
            document_name
        )

        vectorstore = self.vector_manager.load_vector_store(
            vector_path
        )

        results = vectorstore.similarity_search(
            query,
            k=k
        )

        return results
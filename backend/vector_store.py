from langchain_community.vectorstores import FAISS
from backend.embedding import EmbeddingGenerator
from backend.config import VECTOR_DB_PATH


class VectorStoreManager:
    """
    Handles creation, saving, loading and searching of FAISS vector stores.
    """

    def __init__(self):
        self.embedding_model = EmbeddingGenerator().get_embeddings()

    def create_vector_store(self, documents):
        """
        Create a FAISS vector store from document chunks.
        """
        return FAISS.from_documents(
            documents,
            self.embedding_model
        )

    def save_vector_store(self, vectorstore, vector_path=VECTOR_DB_PATH):
        """
        Save FAISS vector store.
        """
        vectorstore.save_local(vector_path)

    def load_vector_store(self, vector_path=VECTOR_DB_PATH):
        """
        Load FAISS vector store.
        """
        return FAISS.load_local(
            vector_path,
            self.embedding_model,
            allow_dangerous_deserialization=True
        )
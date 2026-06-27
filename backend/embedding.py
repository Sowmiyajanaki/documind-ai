from langchain_huggingface import HuggingFaceEmbeddings
from backend.config import EMBEDDING_MODEL


class EmbeddingGenerator:
    """
    Handles creation of HuggingFace embeddings.
    """

    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

    def get_embeddings(self):
        """
        Returns the embedding model.
        """
        return self.embedding_model
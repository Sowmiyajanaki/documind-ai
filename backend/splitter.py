from langchain_text_splitters import RecursiveCharacterTextSplitter
from backend.config import CHUNK_SIZE, CHUNK_OVERLAP


class DocumentSplitter:
    """
    Splits LangChain documents into smaller chunks.
    """

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

    def split_documents(self, documents):
        """
        Split documents into smaller chunks.
        """
        return self.splitter.split_documents(documents)
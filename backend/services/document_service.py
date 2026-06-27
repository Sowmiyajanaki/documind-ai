import os
import shutil

from backend.loader import PDFLoader
from backend.splitter import DocumentSplitter
from backend.vector_store import VectorStoreManager


class DocumentService:
    """
    Handles document upload, processing and FAISS index creation.
    """

    def __init__(self):

        self.loader = PDFLoader()
        self.splitter = DocumentSplitter()
        self.vectorstore = VectorStoreManager()

    def process_document(self, uploaded_file_path):

        # PDF name without extension
        document_name = os.path.splitext(
            os.path.basename(uploaded_file_path)
        )[0]

        # Create vector folder
        vector_path = os.path.join(
            "vectorstore",
            document_name
        )

        os.makedirs(vector_path, exist_ok=True)

        # Load PDF
        documents = self.loader.load_pdf(
            uploaded_file_path
        )

        # Split
        chunks = self.splitter.split_documents(
            documents
        )

        # Create Vector Store
        vector_db = self.vectorstore.create_vector_store(
            chunks
        )

        # Save Vector Store
        vector_db.save_local(vector_path)

        return {
            "document": document_name,
            "pages": len(documents),
            "chunks": len(chunks),
            "vector_path": vector_path
        }
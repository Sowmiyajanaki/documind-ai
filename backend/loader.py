from langchain_community.document_loaders import PyPDFLoader
import os


class PDFLoader:
    """
    Loads PDF documents using LangChain.
    """

    def load_pdf(self, pdf_path):
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF not found: {pdf_path}")

        loader = PyPDFLoader(pdf_path)

        documents = loader.load()

        return documents
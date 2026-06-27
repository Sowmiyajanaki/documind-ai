from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
import os

from backend.services.rag_service import RAGService
from backend.services.document_service import DocumentService

app = FastAPI(
    title="RAG Document QA API",
    version="2.1.0"
)

rag_service = RAGService()
document_service = DocumentService()


class QuestionRequest(BaseModel):
    question: str
    document: str


@app.get("/")
def home():
    return {
        "message": "Welcome to the RAG Document QA API v2.1"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }


@app.get("/dashboard")
def dashboard():

    vectorstore_path = "vectorstore"

    documents = []

    total_chunks = 0

    if os.path.exists(vectorstore_path):

        for folder in os.listdir(vectorstore_path):

            folder_path = os.path.join(
                vectorstore_path,
                folder
            )

            if os.path.isdir(folder_path):

                documents.append(folder)

    return {
        "documents": len(documents),
        "chunks": total_chunks,
        "model": "Llama 3.3 70B",
        "embedding": "MiniLM-L6-v2",
        "status": "Ready"
    }


@app.get("/documents")
def get_documents():

    vectorstore_path = "vectorstore"

    if not os.path.exists(vectorstore_path):

        return {
            "documents": []
        }

    documents = []

    for folder in os.listdir(vectorstore_path):

        folder_path = os.path.join(
            vectorstore_path,
            folder
        )

        if os.path.isdir(folder_path):

            documents.append(folder)

    documents.sort()

    return {
        "documents": documents
    }


@app.post("/chat")
def chat(request: QuestionRequest):

    try:

        return rag_service.ask(
            request.question,
            request.document
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    try:

        os.makedirs(
            "data",
            exist_ok=True
        )

        file_path = os.path.join(
            "data",
            file.filename
        )

        with open(file_path, "wb") as buffer:

            buffer.write(
                await file.read()
            )

        result = document_service.process_document(
            file_path
        )

        return {
            "message": "Upload successful",
            "document": result["document"],
            "pages": result["pages"],
            "chunks": result["chunks"]
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
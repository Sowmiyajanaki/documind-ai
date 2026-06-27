from backend.config import *

print("=" * 50)
print("RAG PROJECT CONFIGURATION")
print("=" * 50)

print("Groq API Loaded :", GROQ_API_KEY is not None)
print("LLM Model       :", LLM_MODEL)
print("Embedding Model :", EMBEDDING_MODEL)
print("Chunk Size      :", CHUNK_SIZE)
print("Chunk Overlap   :", CHUNK_OVERLAP)
print("Upload Folder   :", UPLOAD_FOLDER)
print("Vector DB Path  :", VECTOR_DB_PATH)
print("Data Folder     :", DATA_FOLDER)
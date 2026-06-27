from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# ==========================
# API Configuration
# ==========================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ==========================
# Model Configuration
# ==========================
LLM_MODEL = "llama-3.3-70b-versatile"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ==========================
# Text Chunking
# ==========================
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# ==========================
# Project Paths
# ==========================
UPLOAD_FOLDER = "uploads"
VECTOR_DB_PATH = "vectorstore"
DATA_FOLDER = "data"
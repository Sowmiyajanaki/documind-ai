from backend.loader import PDFLoader
from backend.splitter import DocumentSplitter
from backend.vector_store import VectorStoreManager

print("=" * 60)
print("FAISS VECTOR STORE TEST")
print("=" * 60)

loader = PDFLoader()
documents = loader.load_pdf("data/NIST.pdf")

splitter = DocumentSplitter()
chunks = splitter.split_documents(documents)

print(f"Pages Loaded : {len(documents)}")
print(f"Chunks Created : {len(chunks)}")

manager = VectorStoreManager()

vectorstore = manager.create_vector_store(chunks)

manager.save_vector_store(vectorstore)

print("\n✅ Vector Store Created Successfully!")

print("\nSaved inside:")
print("vectorstore/")

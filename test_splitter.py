from backend.loader import PDFLoader
from backend.splitter import DocumentSplitter

loader = PDFLoader()
documents = loader.load_pdf("data/NIST.pdf")

splitter = DocumentSplitter()
chunks = splitter.split_documents(documents)

print("=" * 50)
print("TEXT SPLITTER TEST")
print("=" * 50)

print("Original Pages :", len(documents))
print("Total Chunks   :", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

print("\nMetadata:\n")
print(chunks[0].metadata)
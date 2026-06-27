from backend.loader import PDFLoader

loader = PDFLoader()

documents = loader.load_pdf("data/NIST.pdf")

print("=" * 50)
print("PDF LOADED SUCCESSFULLY")
print("=" * 50)

print(f"Total Pages: {len(documents)}")

print("\nFirst Page Preview:\n")

print(documents[0].page_content[:500])

print("\nMetadata:\n")

print(documents[0].metadata)

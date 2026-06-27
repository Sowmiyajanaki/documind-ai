from backend.retriever import DocumentRetriever

print("=" * 60)
print("RETRIEVER TEST")
print("=" * 60)

retriever = DocumentRetriever()

query = "What is cloud computing?"

results = retriever.retrieve(query)

print(f"\nQuestion: {query}\n")

print(f"Retrieved {len(results)} documents.\n")

for i, doc in enumerate(results, start=1):
    print("=" * 60)
    print(f"Result {i}")
    print("=" * 60)

    print(doc.page_content[:400])

    print("\nMetadata:")
    print(doc.metadata)
    print()
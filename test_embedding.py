from backend.embedding import EmbeddingGenerator

print("=" * 50)
print("EMBEDDING TEST")
print("=" * 50)

generator = EmbeddingGenerator()

embedding_model = generator.get_embeddings()

text = "What is cloud computing?"

vector = embedding_model.embed_query(text)

print("Input Text:")
print(text)

print("\nVector Length:", len(vector))

print("\nFirst 10 Values:")
print(vector[:10])
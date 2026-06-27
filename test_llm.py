from backend.retriever import DocumentRetriever
from backend.llm import GroqLLM

print("=" * 60)
print("RAG + GROQ TEST")
print("=" * 60)

question = "What is cloud computing?"

retriever = DocumentRetriever()

documents = retriever.retrieve(question)

llm = GroqLLM()

answer = llm.generate_answer(question, documents)

print("\nQuestion:")
print(question)

print("\nAnswer:\n")
print(answer)
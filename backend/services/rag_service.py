from backend.retriever import DocumentRetriever
from backend.llm import GroqLLM
from backend.services.prompt_builder import PromptBuilder
from backend.services.source_formatter import SourceFormatter


class RAGService:
    """
    Main service that coordinates the RAG pipeline.
    """

    def __init__(self):
        self.retriever = DocumentRetriever()
        self.llm = GroqLLM()

    def ask(self, question, document_name):
        """
        Execute the complete RAG pipeline.
        """

        # Retrieve relevant documents
        documents = self.retriever.retrieve(
            question,
            document_name
        )

        # Build prompt
        prompt = PromptBuilder.build_prompt(
            question,
            documents
        )

        # Generate answer
        answer = self.llm.generate_from_prompt(
            prompt
        )

        # Format sources
        sources = SourceFormatter.format_sources(
            documents
        )

        return {
            "question": question,
            "document": document_name,
            "answer": answer,
            "sources": sources
        }


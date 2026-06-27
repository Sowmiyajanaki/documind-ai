class PromptBuilder:
    """
    Builds prompts for the LLM.
    """

    @staticmethod
    def build_prompt(question, documents):

        context = "\n\n".join(
            [doc.page_content for doc in documents]
        )

        prompt = f"""
You are an AI Document Assistant.

Rules:

1. Answer ONLY using the provided context.
2. Do NOT make up information.
3. If the answer is not found, reply:
   "I couldn't find the answer in the uploaded document."
4. Answer clearly using paragraphs or bullet points when appropriate.
5. Mention only information supported by the context.

==================================================

Context:

{context}

==================================================

Question:

{question}

==================================================

Answer:
"""

        return prompt
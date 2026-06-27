from groq import Groq
from backend.config import GROQ_API_KEY, LLM_MODEL


class GroqLLM:
    """
    Handles communication with the Groq LLM.
    """

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate_from_prompt(self, prompt):
        """
        Generate response from a prepared prompt.
        """

        response = self.client.chat.completions.create(
            model=LLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content.strip()
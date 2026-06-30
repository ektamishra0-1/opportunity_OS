import os

import google.generativeai as genai

from .base import BaseLLMClient


class GeminiClient(BaseLLMClient):

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if api_key is None:
            raise ValueError(
                "GEMINI_API_KEY environment variable not found."
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate(self, prompt: str) -> str:

        response = self.model.generate_content(prompt)

        return response.text
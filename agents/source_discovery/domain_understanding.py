import json

from .models import DomainInput, DomainContext


class DomainUnderstanding:

    def __init__(self, llm):
        self.llm = llm

    def understand(
        self,
        request: DomainInput
    ) -> DomainContext:

        prompt = f"""
You are an expert research analyst.

The user wants to explore this domain:

Domain:
{request.domain}

Description:
{request.description}

Your job is to understand this domain.

Return ONLY valid JSON.

Format:

{{
    "keywords": [
        "...",
        "..."
    ],

    "synonyms": [
        "...",
        "..."
    ],

    "related_topics": [
        "...",
        "..."
    ]
}}
"""

        response = self.llm.generate(prompt)

        # Gemini sometimes returns ```json ... ```
        response = response.replace("```json", "")
        response = response.replace("```", "").strip()

        data = json.loads(response)

        return DomainContext(

            domain=request.domain,

            keywords=data["keywords"],

            synonyms=data["synonyms"],

            related_topics=data["related_topics"]

        )
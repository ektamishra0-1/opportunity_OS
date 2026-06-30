import json

from .models import DomainContext, SearchQuery


class SearchPlanner:

    def __init__(self, llm):
        self.llm = llm

    def generate_queries(
        self,
        context: DomainContext
    ) -> list[SearchQuery]:

        prompt = f"""
You are an expert research planner.

The goal is to discover REAL startup opportunities.

Domain:
{context.domain}

Keywords:
{context.keywords}

Related Topics:
{context.related_topics}

Generate EXACTLY 10 search queries that will help find:

- complaints
- bottlenecks
- repetitive work
- manual work
- unmet needs
- feature requests
- discussions
- startup opportunities
- researchers complaining
- industry pain points

Return ONLY JSON.

Example

[
    "query 1",
    "query 2"
]
"""

        response = self.llm.generate(prompt)

        response = response.replace("```json", "")
        response = response.replace("```", "").strip()

        queries = json.loads(response)

        return [

            SearchQuery(query=q)

            for q in queries

        ]
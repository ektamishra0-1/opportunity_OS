import os

from tavily import TavilyClient

from .base import SearchProvider
from agents.source_discovery.models import SearchResult


class TavilySearchProvider(SearchProvider):

    def __init__(self):

        api_key = os.getenv("TAVILY_API_KEY")

        if api_key is None:
            raise ValueError(
                "TAVILY_API_KEY environment variable not found."
            )

        self.client = TavilyClient(api_key=api_key)

    def search(
        self,
        query: str,
        max_results: int = 10
    ) -> list[SearchResult]:

        response = self.client.search(

            query=query,

            search_depth="advanced",

            max_results=max_results

        )

        results = []

        for i, item in enumerate(response["results"]):

            results.append(

                SearchResult(

                    title=item.get("title", ""),

                    url=item.get("url", ""),

                    snippet=item.get("content", ""),

                    rank=i + 1

                )

            )

        return results
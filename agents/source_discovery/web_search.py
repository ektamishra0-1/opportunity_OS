"""
web_search.py

Purpose:
Execute search queries using any supported search provider.

This module should NEVER know whether the search engine is
Tavily, Brave, Google, Bing, etc.

It only depends on the SearchProvider interface.
"""

from abc import ABC, abstractmethod
from typing import List

from .models import SearchQuery, SearchResult


# ============================================================
# Search Provider Interface
# ============================================================

class SearchProvider(ABC):
    """
    Abstract search provider.

    Every search engine implementation must implement
    this interface.
    """

    @abstractmethod
    def search(
        self,
        query: str,
        max_results: int = 10
    ) -> List[SearchResult]:
        pass


# ============================================================
# Web Search Module
# ============================================================

class WebSearch:

    def __init__(self, provider: SearchProvider):
        self.provider = provider

    def search_queries(
        self,
        queries: List[SearchQuery]
    ) -> List[SearchResult]:

        all_results = []

        for query in queries:

            results = self.provider.search(
                query=query.query,
                max_results=10
            )

            all_results.extend(results)

        return all_results
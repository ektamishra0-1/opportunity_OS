from abc import ABC, abstractmethod

from agents.source_discovery.models import SearchResult


class SearchProvider(ABC):

    @abstractmethod
    def search(
        self,
        query: str,
        max_results: int = 10
    ) -> list[SearchResult]:
        pass
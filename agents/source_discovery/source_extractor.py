"""
source_extractor.py

Purpose:
Convert raw SearchResult objects into standardized Source objects.

This module performs NO intelligence.

It only standardizes data so downstream modules
work with a consistent format.
"""

from urllib.parse import urlparse

from .models import (
    SearchResult,
    Source
)


class SourceExtractor:

    def extract(
        self,
        search_results: list[SearchResult]
    ) -> list[Source]:

        sources = []

        for result in search_results:

            source = Source(
                title=result.title.strip(),
                url=result.url.strip(),

                source_type=self._detect_source_type(result.url),

                discovery_reason="Discovered through web search.",

                page_summary=result.snippet.strip()
            )

            sources.append(source)

        return sources

    # --------------------------------------------------------

    def _detect_source_type(
        self,
        url: str
    ) -> str:

        """
        Classify the source based on its domain.

        This is intentionally lightweight.

        Later we can replace this with
        an LLM-based classifier.
        """

        domain = urlparse(url).netloc.lower()

        if "reddit" in domain:
            return "community"

        if "stackoverflow" in domain:
            return "forum"

        if "github" in domain:
            return "code"

        if "arxiv" in domain:
            return "research"

        if "pubmed" in domain:
            return "research"

        if "medium" in domain:
            return "blog"

        if "youtube" in domain:
            return "video"

        if "linkedin" in domain:
            return "professional"

        return "website"
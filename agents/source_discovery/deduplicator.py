"""
deduplicator.py

Purpose:
Prevent the Source Discovery Agent from processing the
same source multiple times.

Responsibilities:
- Normalize URLs
- Detect duplicate URLs
- Track processed sources
"""

from urllib.parse import (
    urlparse,
    urlunparse,
    parse_qsl,
    urlencode
)

from .models import Source


class Deduplicator:

    """
    Removes duplicate sources.

    Future versions can also support:
    - Content hash deduplication
    - Database lookups
    - Redis cache
    """

    TRACKING_PARAMETERS = {

        "utm_source",
        "utm_medium",
        "utm_campaign",
        "utm_term",
        "utm_content",
        "fbclid",
        "gclid",
        "ref"

    }

    def __init__(self):

        self.visited_urls = set()

    # --------------------------------------------------------

    def remove_duplicates(
        self,
        sources: list[Source]
    ) -> list[Source]:

        unique = []

        for source in sources:

            normalized = self.normalize_url(source.url)

            if normalized in self.visited_urls:
                continue

            self.visited_urls.add(normalized)

            source.url = normalized

            unique.append(source)

        return unique

    # --------------------------------------------------------

    def normalize_url(
        self,
        url: str
    ) -> str:

        parsed = urlparse(url)

        query = parse_qsl(
            parsed.query,
            keep_blank_values=True
        )

        filtered_query = [

            (k, v)

            for k, v in query

            if k not in self.TRACKING_PARAMETERS

        ]

        normalized = parsed._replace(

            query=urlencode(filtered_query),

            fragment=""

        )

        return urlunparse(normalized)
"""
source_discovery_agent.py

Public entry point for the Source Discovery Agent.

Other parts of Opportunity OS should interact with this class,
not directly with the SearchManager.
"""

from .models import (
    DomainInput,
    SourceDiscoveryResult
)


class SourceDiscoveryAgent:
    """
    High-level interface for discovering information sources.
    """

    def __init__(self, search_manager):
        self.search_manager = search_manager

    # ---------------------------------------------------------

    def discover(
        self,
        domain: str,
        description: str | None = None,
        max_sources: int = 10,
        search_budget: int = 5,
        quality_threshold: float = 0.70
    ) -> SourceDiscoveryResult:

        request = DomainInput(
            domain=domain,
            description=description,
            max_sources=max_sources,
            search_budget=search_budget,
            quality_threshold=quality_threshold
        )

        return self.search_manager.run(request)
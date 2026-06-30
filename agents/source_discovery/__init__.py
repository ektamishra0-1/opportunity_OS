"""
Source Discovery Agent

This package contains all components required to discover,
evaluate, and rank high-quality information sources for a
given domain.

Pipeline:

DomainInput
    ↓
DomainUnderstanding
    ↓
SearchPlanner
    ↓
WebSearch
    ↓
SourceExtractor
    ↓
Deduplicator
    ↓
SourceEvaluator
    ↓
Reflection
    ↓
SourceDiscoveryResult
"""

from .models import (
    DomainInput,
    DomainContext,
    SearchQuery,
    SearchResult,
    Source,
    SourceDiscoveryResult,
)

from .domain_understanding import DomainUnderstanding

from .search_planner import SearchPlanner

from .web_search import (
    WebSearch,
    SearchProvider,
)

from .source_extractor import SourceExtractor

from .source_evaluator import (
    SourceEvaluator,
    SemanticScorer,
    LLMJudge,
)

from .reflection import (
    Reflection,
    ReflectionDecision,
)

from .deduplicator import Deduplicator

from .search_manager import SearchManager

from .source_discovery_agent import SourceDiscoveryAgent


__all__ = [
    # Models
    "DomainInput",
    "DomainContext",
    "SearchQuery",
    "SearchResult",
    "Source",
    "SourceDiscoveryResult",

    # Modules
    "DomainUnderstanding",
    "SearchPlanner",
    "WebSearch",
    "SourceExtractor",
    "SourceEvaluator",
    "Reflection",
    "Deduplicator",
    "SearchManager",
    "SourceDiscoveryAgent",

    # Interfaces
    "SearchProvider",
    "SemanticScorer",
    "LLMJudge",

    # Reflection
    "ReflectionDecision",
]
"""
reflection.py

Purpose:
Analyse the current search progress and decide
whether the Source Discovery Agent should continue
searching or stop.
"""

from dataclasses import dataclass
from typing import List

from .models import Source


# =====================================================
# Reflection Result
# =====================================================

@dataclass(slots=True)
class ReflectionDecision:

    continue_search: bool

    reason: str

    missing_source_types: List[str]

    suggested_queries: List[str]


# =====================================================
# Reflection Module
# =====================================================

class Reflection:

    """
    Reflection module.

    This is where the agent reasons about its
    own progress.
    """

    def reflect(

        self,

        sources: List[Source],

        iteration: int,

        max_iterations: int,

        target_sources: int

    ) -> ReflectionDecision:

        # ---------------------------------------------
        # Budget exhausted
        # ---------------------------------------------

        if iteration >= max_iterations:

            return ReflectionDecision(

                continue_search=False,

                reason="Maximum search iterations reached.",

                missing_source_types=[],

                suggested_queries=[]

            )

        # ---------------------------------------------
        # Enough high quality sources
        # ---------------------------------------------

        good_sources = [

            s for s in sources

            if s.final_score >= 0.70

        ]

        if len(good_sources) >= target_sources:

            return ReflectionDecision(

                continue_search=False,

                reason="Target number of high-quality sources reached.",

                missing_source_types=[],

                suggested_queries=[]

            )

        # ---------------------------------------------
        # Analyse diversity
        # ---------------------------------------------

        source_types = {

            s.source_type

            for s in sources

        }

        expected = {

            "forum",

            "community",

            "research",

            "news",

            "blog",

            "documentation"

        }

        missing = list(expected - source_types)

        # ---------------------------------------------
        # Ask agent to continue
        # ---------------------------------------------

        return ReflectionDecision(

            continue_search=True,

            reason="Insufficient coverage of the domain.",

            missing_source_types=missing,

            suggested_queries=[]

        )
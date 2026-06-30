"""
source_evaluator.py

Purpose:
Evaluate discovered sources and assign quality scores.

Pipeline:

Heuristics
    ↓
Semantic Similarity
    ↓
LLM Judge
    ↓
Final Weighted Score
"""

from abc import ABC, abstractmethod

from .models import Source


# ==========================================================
# Interfaces
# ==========================================================

class SemanticScorer(ABC):

    @abstractmethod
    def score(
        self,
        source: Source
    ) -> float:
        pass


class LLMJudge(ABC):

    @abstractmethod
    def judge(
        self,
        source: Source
    ) -> tuple[float, str]:
        """
        Returns

        score

        reasoning
        """
        pass


# ==========================================================
# Heuristic Scorer
# ==========================================================

class HeuristicScorer:

    """
    Fast rule-based scoring.

    Cheap.

    Runs first.
    """

    LOW_VALUE_PATHS = [

        "/login",
        "/signup",
        "/register",
        "/privacy",
        "/terms",
        "/cookies",
        "/cart"

    ]

    def score(
        self,
        source: Source
    ) -> float:

        score = 1.0

        url = source.url.lower()

        for path in self.LOW_VALUE_PATHS:

            if path in url:
                score -= 0.4

        return max(score, 0.0)


# ==========================================================
# Final Evaluator
# ==========================================================

class SourceEvaluator:

    def __init__(

        self,

        semantic_scorer: SemanticScorer,

        llm_judge: LLMJudge

    ):

        self.heuristics = HeuristicScorer()

        self.semantic = semantic_scorer

        self.llm = llm_judge

    # ------------------------------------------------------

    def evaluate(
        self,
        sources: list[Source]
    ) -> list[Source]:

        evaluated = []

        for source in sources:

            heuristic = self.heuristics.score(source)

            semantic = self.semantic.score(source)

            llm_score, reasoning = self.llm.judge(source)

            final_score = (

                heuristic * 0.2 +

                semantic * 0.4 +

                llm_score * 0.4

            )

            source.relevance_score = semantic

            source.final_score = final_score

            source.confidence = llm_score

            source.discovery_reason = reasoning

            evaluated.append(source)

        evaluated.sort(

            key=lambda s: s.final_score,

            reverse=True

        )

        return evaluated
from database.models import Problem
from agents.problem_extractor.rules import PROBLEM_KEYWORDS


class ProblemExtractorAgent:

    def classify(self, text):
        text = text.lower()

        for category, keywords in PROBLEM_KEYWORDS.items():

            for keyword in keywords:

                if keyword in text:
                    return category, 0.8

        return "unknown", 0.3

    def extract_problem(self, observation):

        category, confidence = self.classify(
            observation.title
        )

        problem_text = (
            f"Potential issue detected: "
            f"{observation.title}"
        )

        return Problem(
            observation_title=observation.title,
            problem_text=problem_text,
            category=category,
            confidence=confidence
        )
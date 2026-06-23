from database.models import Observation
from agents.problem_extractor.extractor import (
    ProblemExtractorAgent
)

obs = Observation(
    source="github",
    source_id="1",
    title="Application becomes slow with large files",
    content="",
    author="test",
    url="",
    timestamp=""
)

agent = ProblemExtractorAgent()

problem = agent.extract_problem(obs)

print(problem.problem_text)
print(problem.category)
print(problem.confidence)
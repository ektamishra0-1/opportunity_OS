from dotenv import load_dotenv

load_dotenv()

from providers.llm import GeminiClient
from agents.source_discovery.search_planner import SearchPlanner
from agents.source_discovery.models import DomainContext

llm = GeminiClient()

planner = SearchPlanner(llm)

context = DomainContext(
    domain="Data Analysis",
    description="Find market gaps and startup opportunities."
)

queries = planner.generate_queries(context)

for q in queries:
    print(q.query)
from dotenv import load_dotenv
from providers.search import TavilySearchProvider

load_dotenv()

from providers.llm import GeminiClient

from agents.source_discovery.domain_understanding import DomainUnderstanding
from agents.source_discovery.models import DomainInput


llm = GeminiClient()

domain_agent = DomainUnderstanding(llm)

domain = input("Enter a domain: ")

request = DomainInput(

    domain=domain,

    description=""

)

context = domain_agent.understand(request)
from agents.source_discovery.search_planner import SearchPlanner

planner = SearchPlanner(llm)
search = TavilySearchProvider()

queries = planner.generate_queries(context)
all_results = []

for query in queries:

    print(f"\nSearching: {query.query}")

    results = search.search(
        query=query.query,
        max_results=5
    )

    all_results.extend(results)

print()

print("=" * 60)
print("SEARCH QUERIES")
print("=" * 60)

for i, query in enumerate(queries, start=1):

    print(f"{i}. {query.query}")

print()
print()

print("=" * 60)
print("SEARCH RESULTS")
print("=" * 60)

for i, result in enumerate(all_results, start=1):

    print(f"\n[{i}]")

    print(result.title)

    print(result.url)

print("=" * 60)

print("DOMAIN CONTEXT")

print("=" * 60)

print()

print("Keywords")

print(context.keywords)

print()

print("Synonyms")

print(context.synonyms)

print()

print("Related Topics")

print(context.related_topics)
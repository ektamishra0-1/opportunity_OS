from dotenv import load_dotenv

load_dotenv()

from providers.search import TavilySearchProvider

provider = TavilySearchProvider()

results = provider.search(
    "data analysis workflow problems",
    max_results=5
)

for result in results:

    print("=" * 60)

    print(result.title)

    print(result.url)

    print(result.snippet[:300])

"""import os

from dotenv import load_dotenv

load_dotenv()

print("Tavily Key:", os.getenv("TAVILY_API_KEY"))"""
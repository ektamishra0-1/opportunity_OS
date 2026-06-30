from dotenv import load_dotenv

load_dotenv()

from providers.llm import GeminiClient

llm = GeminiClient()

response = llm.generate("Say hello in one sentence.")

print(response)
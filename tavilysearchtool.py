from dotenv import load_dotenv
import os
from langchain_tavily import TavilySearch

load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_API_KEY")

tavily= TavilySearch(max_results=5)
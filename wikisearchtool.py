# WIKIPEDIA SEARCH TOOL
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

wikiWrapper = WikipediaAPIWrapper(top_k_results=2, doc_content_chars_max=10000)
wiki = WikipediaQueryRun(api_wrapper=wikiWrapper,
                          description="Searches for articles on Wikipedia.")


### TOOL FOR ARXIV SEARCH
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper

arxiv_wrapper = ArxivAPIWrapper(top_k_results=2,doc_content_chars_max=10000)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper,
                       description="Searches for academic papers on arXiv.org.")



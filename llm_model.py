from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from arxivtool import arxiv
from wikisearchtool import wiki
from tavilysearchtool import tavily
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


# define the tools
tools = [arxiv, wiki, tavily]
llm = ChatOpenAI(model="o4-mini")
# bind the tools to the LLM
llm_with_tools =llm.bind_tools(tools)
#print(llm_with_tools.invoke("What is the recent news on AI?"))
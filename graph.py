'''
We will create a chatbot using Langgraph which has the below features:
START -> LLM NODE -> LLM TOOL CALL NODE -> END
LLM NODE WILL DECIDE A TOOL CALL NEEDS TO BE MADE OR NOT
IF TOOL CALL IS NEEDED, IT WILL CALL THE TOOL AND RETURN THE RESULT
THE TOOLS WILL BE ARXIV SEARCH, WIKIPEDIA SEARCH, TAVIL SEARCH
IF NO TOOL CALL IS NEEDED, IT WILL RETURN THE RESULT DIRECTLY
'''

from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage # human message, ai message, tool message
from typing import Annotated
from langgraph.graph.message import add_messages   # appends messages into messages list instead of overriding, will keep the history of messages
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from llm_model import llm_with_tools, tools

# define the state of the nodes
class State(TypedDict):
    messages: Annotated[list[AnyMessage],add_messages]  # list of messages, can be human, ai or tool


# time to build the graph

# we will have mainly two nodes one for chatbot one for tool call

# define function for chatbot node
def chatbot(state:State):
    return {"messages":[llm_with_tools.invoke(state["messages"])]}

# build the graph
builder = StateGraph(State)

# now lets add the nodes
builder.add_node("chatbot",chatbot)
builder.add_node("tool_call", ToolNode(tools))

# add edges
builder.add_edge(START,"chatbot")
builder.add_conditional_edges(
    "chatbot",
    tools_condition,
    # The following dictionary lets you tell the builder to interpret the condition's outputs as a specific node
    # It defaults to the identity function
    {"tools":"tool_call", END: END},
)
builder.add_edge("tool_call","chatbot")

graph = builder.compile()
graph_image = graph.get_graph().draw_mermaid_png()
with open("graph.png", "wb") as f:
    f.write(graph_image)
print("Graph image saved as graph.png")

# messages=graph.invoke({"messages":"1706.03762"})
# for m in messages['messages']:
#     m.pretty_print()

for chunk,metadata in graph.stream({"messages":"1706.03762"},stream_mode="messages"):
    if chunk.content:
        print(chunk.content,end="",flush=True)
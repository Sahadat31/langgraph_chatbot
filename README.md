# Langgraph-Tools Chatbot

A terminal‑based, interactive chatbot built on [Langgraph](https://github.com/langgraph/langgraph) and LangChain, with automatic tool routing.  
The bot can decide at runtime whether to answer directly or invoke one of several external “search” tools (ArXiv, Wikipedia or Tavil) and then return the result.

---

## 🚀 Features

- **LLM‑driven dialogue**  
  Uses your chosen LLM (via `llm_with_tools`) to handle natural conversation.
- **Automatic tool calling**  
  The LLM node inspects each user query, and if it needs extra knowledge, it will:
  1. Branch into a ToolNode  
  2. Call one of: ArXiv search, Wikipedia search, or Tavil search  
  3. Return the tool’s output back into the conversation

- **Streaming support** (optional)  
  Swap `invoke` for `stream` to print token‑by‑token output.

---

## 📦 Prerequisites

- Python 3.10+  
- A supported LLM endpoint (e.g. OpenAI API key set via `OPENAI_API_KEY`)  
- A TAVILY_API_KEY
- Install the required packages:
  ```bash
  pip install -r requirements.txt


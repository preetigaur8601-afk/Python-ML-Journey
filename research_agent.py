import warnings
warnings.filterwarnings("ignore")

from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage
from duckduckgo_search import DDGS

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="YOUR_GROQ_KEY"
)

@tool
def search_web(query: str) -> str:
    """Search the web for information about any topic"""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=2)
        output = ""
        for r in results:
            output += r['title'] + " - " + r['body'] + "\n"
        return output

llm_with_tools = llm.bind_tools([search_web])

messages = [HumanMessage("What is Agentic AI?")]
response = llm_with_tools.invoke(messages)
messages.append(response)

tool_call = response.tool_calls[0]
tool_result = search_web.invoke(tool_call['args'])
messages.append(ToolMessage(tool_result, tool_call_id=tool_call['id']))

final_response = llm_with_tools.invoke(messages)
print(final_response.content)

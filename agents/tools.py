from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_linkup import LinkupSearchTool
import os

def get_tools(enabled: bool, tool_choice: str = "tavily"):
    if not enabled:
        return []
    if tool_choice == "linkup":
        return [LinkupSearchTool(
            depth="standard",
            output_type="searchResults",
            linkup_api_key=os.getenv("LINKUP_API_KEY")
        )]
    # Default to Tavily
    return [TavilySearchResults(max_results=2)]

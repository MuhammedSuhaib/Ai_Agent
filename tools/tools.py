# tools\tools.py
from agents import function_tool
from schemas.schemas import SubtractInput


@function_tool(
    name_override="subtract_numbers", description_override="Subtract two numbers"
)
def subtract_numbers(Sub: SubtractInput) -> int:
    """Subtract two numbers."""
    print("Subtracting tool fired 🔥")
    return f"Sub.a - Sub.b: {Sub.a - Sub.b}"


@function_tool(name_override="WebSearchTool", description_override="Search the web")
def WebSearchTool(query: str) -> str:
    """Search the web."""
    print("WebSearchTool fired ==🔥")
    return f"Results for '{query}': ..."

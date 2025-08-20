from agents import Agent, ModelSettings,set_tracing_disabled
from configs.config import model_config
from tools.tools import subtract_numbers
set_tracing_disabled(True)

# Objective: Build an agent that can use a math function as a tool (for example, addition or multiplication).

# Tasks:

# Define a Python function, e.g., def add(a, b): return a + b
# Register this function as a tool with your agent.
# Make the agent able to decide when to use the tool (e.g., “What is 5 + 7?” triggers the function).
# Test the agent with at least three math questions.

# Math Agent
math_agent = Agent(
    name="math_agent",
    instructions=(
        "You are a math agent. Solve math problems in the shortest way. "
    ),
    tools=[subtract_numbers],
    # tool_use_behavior=StopAtTools(['subtract_numbers','']),
    # tool_use_behavior="stop_on_first_tool",
    handoff_description="You are a math teacher",
    model=model_config,
    model_settings=ModelSettings(tool_choice='subtract_numbers',)  #optional
)
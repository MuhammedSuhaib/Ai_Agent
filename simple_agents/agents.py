from agents import Agent, ModelSettings,set_tracing_disabled
from configs.config import model_config
from tools.tools import check_weather,add_numbers
set_tracing_disabled(True)
# Objective: Create an agent that can call more than one function/tool (e.g., math and weather).

# Tasks:

# Add both an add(a, b) and get_weather(city) function as tools.
# Have the agent choose the correct tool based on user input.
# Test with both types of questions.

agent = Agent(
    name="agent",
    instructions=(
        "You are an agent. Solve queries in the shortest way. "
    ),
    tools=[check_weather,add_numbers],
    model=model_config,
    model_settings=ModelSettings(tool_choice='required')  #optional
)
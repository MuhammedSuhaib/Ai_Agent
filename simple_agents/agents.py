from agents import Agent, ModelSettings,set_tracing_disabled
from configs.config import model_config
from tools.tools import check_weather
set_tracing_disabled(True)

# Weather Agent
weather_agent = Agent(
    name="weather_agent",
    instructions=(
        "You are a Weather agent. Solve weather-related queries in the shortest way. "
    ),
    tools=[check_weather],
    handoff_description="You are a weather assistant",
    model=model_config,
    model_settings=ModelSettings(tool_choice='check_weather',)  #optional
)
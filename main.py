from agents import Runner
from simple_agents.agents import weather_agent
import asyncio

async def main():
    output = await Runner.run(starting_agent=weather_agent , input=input('Enter a weather query: '))
    print(output.final_output)

asyncio.run(main())

from agents import Runner
from simple_agents.agents import agent
import asyncio

async def main():
    output = await Runner.run(starting_agent=agent , input=input('Enter your query: '))
    print(output.final_output)

asyncio.run(main())

from agents import Runner
from simple_agents.agents import math_agent
import asyncio

async def main():
    output = await Runner.run(starting_agent=math_agent , input=input())
    print(output.final_output)

asyncio.run(main())

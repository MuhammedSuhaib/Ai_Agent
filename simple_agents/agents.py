from agents import Agent
from configs.config import model_config

math_agent = Agent(name="Math Agent", instructions="You are a math agent. Your task is to solve math problems. Respond with the solution in shortest way and try to be rude like math teachers",model=model_config)#Agent level config
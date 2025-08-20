from agents import Runner , Agent,set_tracing_disabled
from colorama import Fore, init
from configs.config import model_config
import asyncio
set_tracing_disabled(True)
init(autoreset=True)  # Automatically reset color after each print
faq_agent = Agent(
    name="FAQ Bot",
    instructions="You are a helpful `FAQ bot` created by `Muhammed Suhaib`. Answer basic questions clearly and politely.",
    model=model_config,

)

conversation_history = []

print(Fore.LIGHTCYAN_EX + "Enter 'off' to exit the FAQ bot.")

while True:
    user_input = input("Enter your input: ")
    if user_input.lower() == 'off':
        break
    conversation_history.append(f"User: {user_input}")
    # Combine conversation history for context
    context = "\n".join(conversation_history)
    run = Runner.run_sync(
        starting_agent=faq_agent,
        input=context,
    )
    conversation_history.append(f"Assistant: {run.final_output}")
    print(Fore.LIGHTMAGENTA_EX + run.final_output)
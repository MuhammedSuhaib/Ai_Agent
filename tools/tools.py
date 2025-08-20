# tools\tools.py
from agents import function_tool
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("openweathermap")  # make sure this is valid

@function_tool(name_override="check_weather", description_override="Get current weather info")
def check_weather(city: str) -> str:
    """Fetch current weather from OpenWeatherMap."""
    print("check_weather fired ==🔥")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        res = requests.get(url, timeout=5)
        data = res.json()

        if res.status_code == 200:
            return f"Weather in {data['name']}, {data['sys']['country']}: {data['main']['temp']}°C, {data['weather'][0]['description']}"
        else:
            return f"Error {res.status_code}: {data.get('message', 'Unknown error')}"
    except Exception as e:
        return f"Failed to fetch weather: {e}"

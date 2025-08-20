# tools\tools.py
from agents import function_tool
from schemas.schemas import WeatherInput
import os
import requests
from dotenv import load_dotenv
load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


@function_tool(name_override="check_weather", description_override="Get current weather info")
def check_weather(city: WeatherInput) -> str:
    """Fetch current weather from WeatherAPI."""
    print("check_weather fired ==🔥")

    if not WEATHER_API_KEY:
        return "Weather API key not set."

    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if "error" in data:
            return f"API Error: {data['error'].get('message', 'Unknown error')}"

        location = data["location"]["name"]
        country = data["location"]["country"]
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        return f"Weather in {location}, {country}: {temp_c}°C, {condition}"

    except Exception as e:
        return f"Failed to fetch weather: {e}"

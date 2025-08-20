import requests
import os
API_KEY = os.getenv("openweathermap")
city = "Karachi"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

res = requests.get(url)
data = res.json()

if res.status_code == 200:
    print(f"Weather in {data['name']}, {data['sys']['country']}: {data['main']['temp']}°C, {data['weather'][0]['description']}")
else:
    print(f"Error {res.status_code}: {data.get('message')}")

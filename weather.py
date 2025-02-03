from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_weather(city="Jersey City"):
    request_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=imperial"
    response = requests.get(request_url).json()
    return response

if __name__ == "__main__":
    print("\nGet Current Weather Conditions")
    city = input("\nEnter City Name: ")
    if not bool(city.strip()):
        city = "Jersey City"
    
    weather = get_weather(city)

    print("\n")
    pprint(weather)
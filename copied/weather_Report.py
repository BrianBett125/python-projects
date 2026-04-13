"""
weather_report.py
-----------------
A simple Python script that fetches weather data for a given city
using the OpenWeatherMap API.

Author: Brian Bett
Date: 2025-08-27
"""

import requests

# Replace with your own OpenWeatherMap API key
API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name: str) -> dict:
    """Fetch weather details for a given city name."""
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("❌ Error:", response.status_code, response.json())
        return {}


def show_weather(city_name: str):
    """Display the weather in a user-friendly way."""
    data = get_weather(city_name)
    if not data:
        return
    
    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"].capitalize()

    print(f"🌍 Weather Report for {city}, {country}")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"☁️ Condition: {weather}")


if __name__ == "__main__":
    city = input("Enter city name: ")
    show_weather(city)


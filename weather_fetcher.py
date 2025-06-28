import requests

def get_weather(city, api_key):
    """
    Fetch current weather data for a given city using OpenWeatherMap API.

    Args:
        city (str): Name of the city.
        api_key (str): Your OpenWeatherMap API key.

    Returns:
        dict: Weather data or None if an error occurred.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            "City": data["name"],
            "Temperature": f"{data['main']['temp']} °C",
            "Weather": data["weather"][0]["description"].capitalize(),
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Error fetching weather: {err}")
    except KeyError:
        print("Unexpected response format.")
    return None

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    city_name = input("Enter a city name: ")
    weather_info = get_weather(city_name, API_KEY)

    if weather_info:
        print("\nWeather Report:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")
    else:
        print("Could not retrieve weather data.")


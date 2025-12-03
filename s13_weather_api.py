import json
import os
import urllib.request

from dotenv import load_dotenv

load_dotenv()
APIKEY = os.getenv("OPENWEATHER_API_KEY")
# Make sure to set this in your .env file which is under root folder


def get_temperature(city, country_code="us"):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}&units=metric"
    with urllib.request.urlopen(url) as response:
        response_text = response.read().decode("utf-8")
        weather_data = json.loads(response_text)
    temperature = weather_data["main"]["temp"]
    return temperature


def main():
    city = input("Enter city name: ")
    country_code = input("Enter country code (e.g., us for USA): ")
    try:
        temperature = get_temperature(city, country_code)
        print(f"The current temperature in {city}, {country_code} is {temperature}°C.")
    except Exception as e:
        print(
            "An error occurred while fetching the weather data. Please check the city and country code."
        )
        print(f"Error details: {e}")


main()

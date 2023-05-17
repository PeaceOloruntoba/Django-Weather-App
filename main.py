import requests
import json

def get_weather_forecast(city):
    # weather_api key
    api_key = "45b01a7f6a9893cc9370a6fd91f105fb"
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    # Send GET request to OpenWeatherMap API
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Extract relevant information from the API response
        weather = data['weather'][0]['main']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Print the weather forecast
        print(f"Weather forecast for {city}:")
        print(f"  - Weather: {weather}")
        print(f"  - Temperature: {temperature}°C")
        print(f"  - Humidity: {humidity}%")
        print(f"  - Wind Speed: {wind_speed} m/s")
    else:
        print("Error occurred while fetching weather forecast.")

# Example usage:
city_name = input("Enter city name: ")
get_weather_forecast(city_name)

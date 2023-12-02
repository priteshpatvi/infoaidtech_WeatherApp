import requests
import json

# Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'

def fetch_weather_data(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    return data

def display_weather_data(data):
    if data["cod"] == 200:
        weather_info = data["weather"][0]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        weather_condition = weather_info["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Weather Condition: {weather_condition}")
    else:
        print("City not found. Please check the city name.")

def main():
    print("Welcome to the Weather App!")

    while True:
        city_name = input("Enter a city name (or 'quit' to exit): ")

        if city_name.lower() == 'quit':
            print("Goodbye!")
            break

        weather_data = fetch_weather_data(city_name)
        display_weather_data(weather_data)

if __name__ == "__main__":
    main()

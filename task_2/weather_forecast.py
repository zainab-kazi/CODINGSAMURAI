import requests
import json

def weather_fc():

    api_key = "c0093c606cf9edab49f9f836f34623f8"

    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    
    cityName = input("Enter your city: ")
    
    completeURL = baseURL + "q=" + cityName + "&appid=" + api_key

    response = requests.get(completeURL)

    data = response.json()
    
    try:
        print("Current Temperature ",data["main"]["temp"])
        print("Current Temperature Feels ",data["main"]["feels_like"])
        print("Maximum Temperature ",data["main"]["temp_max"])
        print("Minimum Temperature ",data["main"]["temp_min"])
    
    except KeyError:
        print("Weather data not found in specific city.")


if __name__ == "__main__":
    weather_fc()

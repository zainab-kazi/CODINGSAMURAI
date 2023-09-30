import requests
import json

def weather_fc():

    api_key = "c0093c606cf9edab49f9f836f34623f8"

    baseURL = "http://api.openweathermap.org/data/2.5/weather?"
    
    cityName = input("Enter your city: ")
    print("Type C for Celsius and F for Farenheit.")
    temp_conv = input("Temperature in Celsius or Fahrenheit: ")
    
    completeURL = baseURL + "q=" + cityName + "&appid=" + api_key

    response = requests.get(completeURL)

    data = response.json()
    
    try:
        if temp_conv == "C":
            temperature = data["main"]["temp"] - 273.15
            print("Current Temperature: {:.2f}°C".format(temperature))
            print("Current Temperature Feels: {:.2f}°C".format(data["main"]["feels_like"] - 273.15))
            print("Maximum Temperature: {:.2f}°C".format(data["main"]["temp_max"] - 273.15))
            print("Minimum Temperature: {:.2f}°C".format(data["main"]["temp_min"] - 273.15))
    
               
        elif temp_conv == "F":
            temperature = (data["main"]["temp"] - 273.15) * 9/5 + 32
            print("Current Temperature: {:.2f}°F".format(temperature))
            print("Current Temperature Feels: {:.2f}°F".format((data["main"]["feels_like"] - 273.15)*9/5 + 32))
            print("Maximum Temperature: {:.2f}°F".format((data["main"]["temp_max"] - 273.15)*9/5 + 32))
            print("Minimum Temperature: {:.2f}°F".format((data["main"]["temp_min"] - 273.15)*9/5 + 32))
    
               
        else:
            print("Invalid input given!")
    
        
    except KeyError:
        print("Weather data not found in specific city.")


if __name__ == "__main__":
    weather_fc()

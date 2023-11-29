#1
import json
import requests

request = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(request)
    if response.status_code == 200:
        answer = response.json()

        #print(json.dumps(answer, indent=2))
        print(answer["value"])
    else:
        print("There was an error with the server", response.status_code)
except requests.exceptions.ConnectionError as e:
    print("Request could not be completed: " + str(e))

#2
import requests

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        weather_data = response.json()
        description = weather_data['weather'][0]['description']
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = kelvin_to_celsius(temperature_kelvin)

        return description, temperature_celsius

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None

def main():
    api_key = "785ef34b835b34387ce99a72d32157ca"  # Replace with your actual API key
    city_name = input("Enter the name of a municipality: ")

    description, temperature = get_weather(api_key, city_name)

    if description is not None and temperature is not None:
        print(f"Weather in {city_name}: {description}")
        print(f"Temperature: {temperature:.2f} °C")
    else:
        print("Failed to retrieve weather information.")

if __name__ == "__main__":
    main()

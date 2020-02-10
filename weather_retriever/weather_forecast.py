from configparser import ConfigParser
import requests
import argparse

config_parser = ConfigParser()
config_parser.read("config_sample.ini")
username = config_parser.get('auth', 'username')
apikey = config_parser.get('auth', 'apikey')

def weather_api(url_weather, location_code, apikey, unit):
    url_weather = url_weather + location_code + "?apikey=" + apikey + "&details=true"
    response = requests.get(url_weather)
    response_list = response.json()
    if unit == "C":
        print(response_list[0]["ApparentTemperature"]["Metric"]["Value"])
    elif unit == "F":
        print(response_list[0]["ApparentTemperature"]["Imperial"]["Value"])
    else:
        print("Invalid Unit!")

def api_call(url_location, url_weather, city, state, apikey):
    url_location = url_location + apikey + "&q=" + city + "%2C%20" + state 
    response = requests.get(url_location)
    response_list = response.json()
    location_code = response_list[0]["Key"]
    if location_code:
        weather_api(url_weather, location_code, apikey, unit)
    else:
        print("Location not found.")

if __name__ == "__main__":
    url_location = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey="
    url_weather = "http://dataservice.accuweather.com/currentconditions/v1/" 

    parser = argparse.ArgumentParser(description="Weather Forecast")
    parser.add_argument("-c", "--city", help="City name")
    parser.add_argument("-s", "--state", help="State name")
    parser.add_argument("-u", "--unit", help="Temperature unit")
    args = parser.parse_args()
    if args.city: 
        city = args.city
    if args.state:
        state = args.state
    if args.unit:
        unit = args.unit

    api_call(url_location, url_weather, city, state, apikey)

import requests

city = "Toronto"
url = "http://api.weatherapi.com/v1/current.json?key=fb9bd49fff4e4abe8ae152200260409&q=" + city + "&aqi=no"
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get("current").get("temp_c")
description = weather_json.get("current").get("condition").get("text")

print("Today's weather in", city, "is", description, "and", temp, "degrees Celsius.")

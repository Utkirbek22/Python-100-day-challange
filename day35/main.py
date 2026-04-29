import requests
import os

api_key = os.environ.get("owm_api_key")
parametrs = {
    "lat": 52.239018,
    "lon": 21.020176,
    "appid": api_key,
    "cnt": 4,
}


api_key = "0ea7ac9a261c5a93471a2cbec0f6050a"

# https://api.openweathermap.org/data/2.5/weather?lat=52.239018&lon=21.020176&appid=0ea7ac9a261c5a93471a2cbec0f6050a

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parametrs)
print(response.status_code)
data = response.json()
print(data)
will_rain = False
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("bring umbrella")



import requests


ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'

weather_params = {
    "lat": 25.933149,
    "lon": -80.162544,
    "appid": '7c90e9279763e4167f6c6d92c90bdfed'
}

response = requests.get(ENDPOINT, params=weather_params)
print(response.json())
import requests
import os

# weather API
WEATHER_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'

#Telegram bot creds
BOT_TOKEN = os.environ.get("BOT_TOKEN")
TELE_ENDPOINT = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
CHAT_ID = os.environ.get("CHAT_ID")


# to get chat id, just need to request to this url after user sends a message https://api.telegram.org/bot{BOT_TOKEN}/sendMessage

weather_params = {
    "lat": 25.933149,
    "lon": -80.162544,
    "appid": '7c90e9279763e4167f6c6d92c90bdfed',
    "cnt": 4,
}

# requesting weather data from API
response = requests.get(WEATHER_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# getting the weather ID and figuring out if it will rain
will_rain = False
for hour in weather_data['list']:
    weather_id = hour['weather'][0]['id']
    if weather_id < 700:
        will_rain = True

# method to send message on tele bot
def send_message():
    tele_params = {
    'chat_id': CHAT_ID,
    'text': "I'ts going to rain today. Bring an umbrella!",
    }
    r = requests.get(TELE_ENDPOINT, params=tele_params)
    print(r.json())

if will_rain:
    send_message()


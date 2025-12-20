import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

api_key = os.getenv("DAY35_API_KEY")
lat = os.getenv("DAY35_LATITUDE")
lon = os.getenv("DAY35_LONGITUDE")
account_sid = os.getenv("DAY35_ACCOUNT_SID")
auth_token = os.getenv("DAY35_AUTH_TOKEN")
my_phone_number = os.getenv("DAY35_PHONE_NUMBER")

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": str(api_key),
    "cnt": 4
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

hours_id_list = [weather_data["list"][i]["weather"][0]["id"] for i in range(0, 4)]
for id in hours_id_list:
    if int(id) < 600:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body= "Bring an ☔.",
            from_='whatsapp:+14155238886',
            to=my_phone_number
        )
        print(message.status)
        break
    elif int(id) < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body= "Wow! it's ❄️ today!",
            from_='whatsapp:+14155238886',
            to=my_phone_number
        )
        print(message.status)
        break


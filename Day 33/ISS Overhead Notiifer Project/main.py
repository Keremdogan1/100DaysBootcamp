import requests
import os
from dotenv import load_dotenv
import datetime
import smtplib
import time

load_dotenv()

my_lat = float(os.getenv("DAY33_LATITUDE"))
my_lng = float(os.getenv("DAY33_LONGITUDE"))

email = os.getenv("DAY32_EMAIL")
password = os.getenv("DAY32_APP_PASSWORD")
smtp = os.getenv("DAY32_SMTP")

def iss_is_close():

    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if abs(my_lat-iss_latitude) <= 5 and abs(my_lng-iss_longitude) <= 5:
        return 1
    else:
        return 0

def it_is_dark():

    parameters = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    time_now = datetime.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return 1
    else:
        return 0
    
while True:
    time.sleep(60)

    if iss_is_close() and it_is_dark():
        with smtplib.SMTP(smtp, port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(email, email, msg="Subject:Look Up!!\n\nThe ISS is above you in the sky.")
    else:
        print("Maybe next time!")
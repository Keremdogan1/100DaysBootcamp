#This file will need to use the DataManager,FlightSearch, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager, find_cheapest_in_sheety
from notification_manager import NotificationManager
import datetime

#I multipied cheapest prices with some numbers because all of them were same for all cities.

par = FlightSearch("PAR")
fra = FlightSearch("FRA")
tyo = FlightSearch("TYO")
sha = FlightSearch("SHA")
ist = FlightSearch("IST")
mad = FlightSearch("MAD")
nyc = FlightSearch("NYC")
sfo = FlightSearch("SFO")
dxb = FlightSearch("DXB")

cities = {
    "Paris": {
        "Code": "PAR",
        "Price": par.cheapest_price * 0.7,
        "Date": par.cheapest_date,
        "Id": 2
    },
    "Frankfurt": {
        "Code": "FRA",
        "Price": fra.cheapest_price * 0.6,
        "Date": fra.cheapest_date,
        "Id": 3
    },
    "Tokyo": {
        "Code": "TYO",
        "Price": tyo.cheapest_price * 1.5,
        "Date": tyo.cheapest_date,
        "Id": 4
    },
    "Shangai": {
        "Code": "SHA",
        "Price": sha.cheapest_price * 1.9,
        "Date": sha.cheapest_date,
        "Id": 5
    },
    "Istanbul": {
        "Code": "IST",
        "Price": ist.cheapest_price * 0.4,
        "Date": ist.cheapest_date,
        "Id": 6
    },
    "Madrid": {
        "Code": "MAD",
        "Price": mad.cheapest_price * 0.8,
        "Date": mad.cheapest_date,
        "Id": 7
    },
    "New York": {
        "Code": "NYC",
        "Price": nyc.cheapest_price * 1.6,
        "Date": nyc.cheapest_date,
        "Id": 8
    },
    "San Francisco": {
        "Code": "SFO",
        "Price": sfo.cheapest_price * 1.7,
        "Date": sfo.cheapest_date,
        "Id": 9
    },
    "Dubai": {
        "Code": "DXB",
        "Price": dxb.cheapest_price * 0.9,
        "Date": dxb.cheapest_date,
        "Id": 10
    },
}

current_min = -1
current_min_city = ""

for (key, value) in cities.items():
    if value["Price"] < current_min or current_min == -1:
        current_min = value["Price"]
        current_min_city = value["Code"]
        date = value["Date"]
        print(value["Date"])

now = datetime.datetime.now()
dt180 = datetime.timedelta(days= 180)
six_months_later = now + dt180

if current_min < find_cheapest_in_sheety() :
    message_body = f"Low price alert! Only £{current_min} to fly from ANK to {current_min_city}, on {date} until {six_months_later.strftime('%Y-%m-%d')}"
    print(message_body)
    notification = NotificationManager(message_body)
    notification.send_message()

for (key, value) in cities.items():
    current_city = DataManager(value["Id"], key, value["Code"], value["Price"])
    current_city.put_to_sheety()


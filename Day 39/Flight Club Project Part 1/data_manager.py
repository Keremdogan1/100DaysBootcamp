import os
from dotenv import load_dotenv
import requests

load_dotenv()

sheety_token = os.getenv("DAY39_SHEETY_TOKEN")
sheety_endpoint = os.getenv("DAY39_SHEETY_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, id, city, code, price):
        self.id = id
        self.city = city
        self.code = code
        self.price = price

        self.cheapest_price = find_cheapest_in_sheety()

    def put_to_sheety(self):
        put_config = {
            "price": {
                "city": self.city,
                "iataCode": self.code,
                "lowestPrice": self.price
            }
        }

        headers = {
            "Authorization": f"Bearer {sheety_token}"
        }

        response = requests.put(url=f"{sheety_endpoint}/{self.id}", json=put_config, headers=headers)
        print(response.text)

def find_cheapest_in_sheety():
    headers = {
        "Authorization": f"Bearer {sheety_token}"
    }

    response = requests.get(url=sheety_endpoint, headers=headers)
    data = response.json()["prices"]
        
    min = -1

    for city in data:
        if float(city["lowestPrice"]) < min or min == -1:
            min = float(city["lowestPrice"])
        
    print(min)
    return min



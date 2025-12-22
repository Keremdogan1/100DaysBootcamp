import os
from dotenv import load_dotenv
import requests
import datetime

load_dotenv()

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city_code = city
        self.base_url = "https://test.api.amadeus.com"
        self.api_key = os.getenv("DAY39_AMADEUS_API_KEY")
        self.api_secret = os.getenv("DAY39_AMADEUS_API_SECRET")

        self.token = self.get_token()
        self.access_token = self.token["access_token"]

        # Tek seferde çağırıyoruz
        cheapest_price, cheapest_date = self.get_cheapest_flight()
        self.cheapest_price = cheapest_price
        self.cheapest_date = cheapest_date

    def get_token(self):
        data = {
            "client_id": self.api_key,
            "client_secret": self.api_secret,
            "grant_type": "client_credentials"
        }

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        token = requests.post(
            url=f"{self.base_url}/v1/security/oauth2/token",
            headers=headers,
            data=data
        )
        return token.json()
    
    def get_cheapest_flight(self):
        now = datetime.datetime.now()
        dt1 = datetime.timedelta(days=1)
        dt14 = datetime.timedelta(days=14)
        dt180 = datetime.timedelta(days=180)

        current_date = now + dt1
        six_months_later = now + dt180

        min_price = float("inf")
        cheapest_date = None

        while current_date < six_months_later:
            parameters = {
                "originLocationCode": "ANK",
                "destinationLocationCode": "TYO",
                "departureDate": f"{current_date.strftime('%Y-%m-%d')}",
                "adults": 1,
                "currencyCode": "GBP"
            }

            headers = {
                "Authorization": f"Bearer {self.access_token}",
            }
            response = requests.get(
                url=f"{self.base_url}/v2/shopping/flight-offers",
                params=parameters,
                headers=headers
            )
            
            flight_data = response.json()
            lowest_price = float(flight_data["data"][0]["price"]["total"])
            
            if lowest_price < min_price:
                min_price = lowest_price
                cheapest_date = current_date.strftime('%Y-%m-%d')
                print(f"New cheapest price for {self.city_code}: {min_price} on {cheapest_date}")

            current_date += dt14

        print(f"The process ended for {self.city_code}\n")

        return (min_price, cheapest_date)
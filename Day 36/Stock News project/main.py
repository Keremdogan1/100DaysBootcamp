STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client

load_dotenv()

alpha_vantage_api_key = os.getenv("DAY36_ALPHA_VANTAGE_API_KEY")
news_api_key = os.getenv("DAY36_NEWS_API_KEY")
account_sid = os.getenv("DAY35_ACCOUNT_SID")
auth_token = os.getenv("DAY35_AUTH_TOKEN")
my_phone_number = os.getenv("DAY35_PHONE_NUMBER")

alpha_vantage_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "outputsize": "compact",
    "apikey": alpha_vantage_api_key
}

alpha_vantage_response = requests.get(url="https://www.alphavantage.co/query", params=alpha_vantage_parameters)
alpha_vantage_response.raise_for_status()
alpha_vantage_data = alpha_vantage_response.json()["Time Series (Daily)"]
alpha_vantage_data_list = [value for (key, value) in alpha_vantage_data.items()]

yesterday_close = float(alpha_vantage_data_list[0]["4. close"])
the_day_before_yesterday_close = float(alpha_vantage_data_list[1]["4. close"])

change_by_percentage = round(100 * ((yesterday_close - the_day_before_yesterday_close) / ((yesterday_close + the_day_before_yesterday_close) / 2)), 2)
if abs(change_by_percentage) >= 5:
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "sortBy": "publishedAt",
        "apiKey": news_api_key,
        "pageSize": 3,
        "language": "en"
    }

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    
    icon = ""
    if change_by_percentage > 0:
        icon = "🔺"
    else:
        icon = "🔻"
    
    message_body = f"TSLA: {icon}{change_by_percentage}%\n"
    for i in range(0, 3):
        message_body += f"Headline: {news_data["articles"][i]["title"]}\nBrief: {news_data["articles"][i]["description"]}\nLink: {news_data["articles"][i]["url"]}\n\n"
        
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body = message_body,
        from_ = 'whatsapp:+14155238886',
        to = my_phone_number
    )
    print(message.status)

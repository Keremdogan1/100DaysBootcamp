from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv
import re
from email.mime.text import MIMEText

load_dotenv()

email = os.getenv("DAY47_EMAIL")
password = os.getenv("DAY47_APP_PASSWORD")
smtp = os.getenv("DAY47_SMTP")
url = "https://www.amazon.com.tr/Casio-Casiotone-piyano-klavyesi-siyah/dp/B091PD782Y/ref=sr_1_11?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-11"

target_price = 8000

response = requests.get(url=url, headers={"Accept-Language": "tr-TR,tr;q=0.7"})
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

product_title = re.sub(" +", " ", soup.select_one(selector="#productTitle").get_text())
product_title = "".join(product_title.splitlines())
product_title = product_title.strip()
print(product_title)

price = soup.select_one(selector=".a-offscreen").get_text()
price_by_number = int(price.split(".")[0]) * 1000 + int(price.split(".")[1].split(",")[0])
print(price_by_number)

content = f"{product_title} is now {price}!\n{url}"

if price_by_number < target_price:
    with smtplib.SMTP(smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)

        msg = MIMEText(content, "plain", "utf-8")
        msg["Subject"] = "Amazon Price Alert!"
        msg["From"] = email
        msg["To"] = email

        connection.sendmail(from_addr=email, to_addrs=email, msg=msg.as_string())    

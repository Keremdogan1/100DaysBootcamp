import datetime as dt
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("DAY32_EMAIL")
password = os.getenv("DAY32_APP_PASSWORD")
smtp = os.getenv("DAY32_SMTP")

with open("quotes.txt") as quotes:
    lines = quotes.readlines()
    random_quote = lines[random.randint(1,102)]

today = dt.datetime.now().weekday()
if today == 0:
    message =f"Subject:Motivotional Quote for This Monday\n\n{random_quote}"

    with smtplib.SMTP(smtp, port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email, to_addrs="python1test2@yahoo.com", msg=message)
else:
    print("Today wasn't monday, maybe another time!")
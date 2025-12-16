import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("DAY32_EMAIL")
password = os.getenv("DAY32_APP_PASSWORD")
smtp = os.getenv("DAY32_SMTP")


with smtplib.SMTP(smtp, port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs="python1test2@yahoo.com", msg="Subject:Test\n\nHello, this is a test message.")

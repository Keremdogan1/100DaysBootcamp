import datetime as dt
import pandas
import random
import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

email = os.getenv("DAY32_EMAIL")
password = os.getenv("DAY32_APP_PASSWORD")
smtp = os.getenv("DAY32_SMTP")

now = dt.datetime.now()
current_month = now.month
current_day = now.day

data = pandas.read_csv("birthdays.csv")
for index, row in data.iterrows():
    if row["month"] == current_month and row["day"] == current_day:
        selected_letters_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"
        with open(selected_letters_path, "r", encoding="utf-8") as birthday_letter:
            content = birthday_letter.read()
            content = content.replace("[NAME]", row["name"])

            email_address = row["email"]

            with smtplib.SMTP(smtp, port=587) as connection:
                connection.starttls()
                connection.login(user=email, password=password)

                msg = MIMEText(content, "plain", "utf-8")
                msg["Subject"] = f"Doğum Günün Kutlu Olsun {row['name']}!"
                msg["From"] = email
                msg["To"] = email_address

                connection.sendmail(email, email_address, msg.as_string())


            print(content)

        
        



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.





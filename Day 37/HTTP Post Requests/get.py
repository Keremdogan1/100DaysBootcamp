import os
import requests
import json
from datetime import *
from dotenv import load_dotenv

load_dotenv()

pixela_token = os.getenv("DAY37_PIXELA_TOKEN")
pixela_username = os.getenv("DAY37_PIXELA_USERNAME")
graph_id = "graph1"

headers = {"X-USER-TOKEN": pixela_token}

start_date = datetime(2025, 12, 21)
end_date = datetime.now()

for i in range((end_date - start_date).days + 1):
    day = start_date + timedelta(days=i)
    date_str_api = day.strftime("%Y%m%d")       
    date_str_print = day.strftime("%d/%m/%Y")   

    url = f"https://pixe.la/v1/users/{pixela_username}/graphs/{graph_id}/{date_str_api}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "optionalData" in data and data["optionalData"]:
            print(f"Date: {date_str_print}")
            try:
                opt = json.loads(data["optionalData"])
                print(json.dumps(opt, indent=2, ensure_ascii=False))
            except Exception:
                print("Raw optionalData:", data["optionalData"])
            print("-" * 40)
            
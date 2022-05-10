import requests
from datetime import datetime
import os

GENDER = YOUR GENDER
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
NUTRITIONIX_ENDPONT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.getenv('SHEET_ENDPOINT')
TOKEN = os.getenv('TOKEN')

user_input = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-usesr-id": "0"
}

parameters = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=NUTRITIONIX_ENDPONT, headers=headers, json=parameters)
result = response.json()

now = datetime.now()
today_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%X")

sheet_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

print(result)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=sheet_headers)

    print(sheet_response.text)
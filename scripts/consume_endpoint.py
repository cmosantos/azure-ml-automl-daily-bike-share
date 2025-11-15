import json
import requests

endpoint = "<YOUR_ENDPOINT_URL>"
api_key = "<YOUR_API_KEY>"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

with open("../data/sample_input.json", "r", encoding="utf-8") as f:
    payload = json.load(f)

response = requests.post(endpoint, headers=headers, json=payload)
print(response.json())

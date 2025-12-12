import os
import requests

BASE = os.getenv("SANTANDER_API_BASE")
KEY = os.getenv("SANTANDER_API_KEY")

def send_marketing_message(user_id: int, message: str):
    url = f"{BASE}/messages"
    payload = {
        "user_id": user_id,
        "message": message
    }
    headers = {
        "Authorization": f"Bearer {KEY}",
        "Content-Type": "application/json"
    }
    resp = requests.post(url, json=payload, headers=headers)
    resp.raise_for_status()
    return resp.json()

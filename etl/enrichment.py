import os
import requests

BASE = os.getenv("SANTANDER_API_BASE")
KEY = os.getenv("SANTANDER_API_KEY")

def fetch_user_profile(user_id: int):
    headers = {
        "Authorization": f"Bearer {KEY}",
        "Accept": "application/json"
    }
    url = f"{BASE}/users/{user_id}"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

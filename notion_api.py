# src/notion_api.py

import requests
import os
from datetime import datetime

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

def create_page(event):
    url = "https://api.notion.com/v1/pages"

    headers = {
        "Authorization": f"Bearer {NOTION_TOKEN}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Name": {
                "title": [
                    { "text": { "content": event["title"] or "Untitled Event" } }
                ]
            },
            "Start": {
                "date": { "start": event["start"] }
            },
            "End": {
                "date": { "start": event["end"] }
            }
        }
    }

    res = requests.post(url, headers=headers, json=data)
    print(f"📤 Pushed: {event['title']} | Status: {res.status_code}")
    print(f"🧾 Response: {res.text}")

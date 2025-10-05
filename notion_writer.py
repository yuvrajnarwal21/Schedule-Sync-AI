# src/notion_writer.py

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def create_event(title, start_time, end_time):
    url = "https://api.notion.com/v1/pages"
    data = {
        "parent": { "database_id": DATABASE_ID },
        "properties": {
            "Name": {
                "title": [{
                    "text": { "content": title }
                }]
            },
            "Start": {
                "date": { "start": start_time }
            },
            "End": {
                "date": { "start": end_time }
            }
        }
    }

    response = requests.post(url, headers=HEADERS, json=data)

    if response.status_code == 200 or response.status_code == 201:
        print(f"✅ Created event: {title}")
    else:
        print(f"❌ Failed to create event: {title}")
        print(response.status_code)
        print(response.text)

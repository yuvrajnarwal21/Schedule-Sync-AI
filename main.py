import os
from dotenv import load_dotenv
from src.ocr import extract_text_from_image
from src.parser import parse_schedule
from src.notion_api import create_page

load_dotenv()

def push_events_to_notion(events):
    notion_token = os.getenv("NOTION_TOKEN")
    database_id = os.getenv("NOTION_DATABASE_ID")

    for event in events:
        event["notion_token"] = notion_token
        event["notion_database_id"] = database_id
        create_page(event)

if __name__ == "__main__":
    print("[1] Extracting text from image...")
    extracted_text = extract_text_from_image("assets/schedule.png")
    print("Extracted Text:\n", extracted_text)

    print("\n[2] Parsing schedule...")
    events = parse_schedule(extracted_text)
    for event in events:
        print(event)

    print("\n[3] Pushing events to Notion...")
    push_events_to_notion(events)
    print("✅ Done.")

from src.notion_writer import create_event

# Example test
create_event("Test Event", "2025-10-04T11:15:00", "2025-10-04T11:48:00")

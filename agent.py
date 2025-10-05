from src.ocr import extract_text
from src.parser import parse_schedule_text
from src.notion_api import NotionSync

class ScheduleAgent:
    def __init__(self, notion_token, database_id):
        self.notion = NotionSync(notion_token, database_id)

    def run(self, image_path):
        print("[Agent] Processing image...")
        text = extract_text(image_path)
        print("[Agent] Extracted text:", text)

        print("[Agent] Parsing schedule...")
        events = parse_schedule_text(text)
        if not events:
            print("[Agent] No events detected. Exiting.")
            return

        print("[Agent] Syncing with Notion...")
        for event in events:
            self.notion.create_event(event["title"], event["iso"])

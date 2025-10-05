import re
from datetime import datetime, timedelta

# Map weekday names to actual upcoming dates
def get_date_for_day(day_name):
    today = datetime.today()
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    target = days.index(day_name[:3].capitalize())

    days_ahead = (target - today.weekday() + 7) % 7
    return today + timedelta(days=days_ahead)

def parse_schedule(text):
    lines = text.split('\n')
    events = []
    current_day = None

    for line in lines:
        day_match = re.match(r"^\s*(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)", line, re.IGNORECASE)
        if day_match:
            current_day = day_match.group(1)[:3]  # e.g., "Mon"
            continue

        time_match = re.match(r"^\s*(\(?\d{1,2}:\d{2}\s*[APMapm\.]{2,4})\s*[-–~]\s*(\d{1,2}:\d{2}\s*[APMapm\.]{2,4})\)?\s*(.+)", line)
        if time_match and current_day:
            start_str, end_str, title = time_match.groups()
            start_str = start_str.strip().replace('.', '')
            end_str = end_str.strip().replace('.', '')

            # Build ISO datetime
            event_date = get_date_for_day(current_day).date()
            try:
                start_dt = datetime.strptime(f"{event_date} {start_str}", "%Y-%m-%d %I:%M %p")
                end_dt = datetime.strptime(f"{event_date} {end_str}", "%Y-%m-%d %I:%M %p")
                events.append({
                    "title": title.strip(),
                    "start": start_dt.isoformat(),
                    "end": end_dt.isoformat()
                })
            except Exception as e:
                print("❌ Time parsing error:", e)
                continue

    return events
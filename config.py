import os
import json

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

SHEET_ID = os.getenv("SHEET_ID")

GOOGLE_CREDENTIALS = json.loads(
    os.getenv("GOOGLE_CREDENTIALS")
)

TOTAL_QUESTIONS = 15
QUIZ_DURATION = 120

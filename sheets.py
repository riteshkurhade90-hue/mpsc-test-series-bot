import json
import gspread
from google.oauth2.service_account import Credentials

from config import SHEET_ID, GOOGLE_CREDENTIALS

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = Credentials.from_service_account_info(
    GOOGLE_CREDENTIALS,
    scopes=SCOPES
)

client = gspread.authorize(credentials)

spreadsheet = client.open_by_key(SHEET_ID)

questions_sheet = spreadsheet.worksheet("Questions")
results_sheet = spreadsheet.worksheet("Results")
def get_questions(day):
    rows = questions_sheet.get_all_records()

    questions = []

    for row in rows:
        if int(row["Day"]) == int(day):
            questions.append(row)

    return questions


def save_result(user_id, name, username, day, correct, wrong, percentage, time_taken, submitted_at):
    results_sheet.append_row([
        user_id,
        name,
        username,
        day,
        correct,
        wrong,
        percentage,
        time_taken,
        submitted_at
    ])


def get_top3(day):
    rows = results_sheet.get_all_records()

    filtered = []

    for row in rows:
        if int(row["Day"]) == int(day):
            filtered.append(row)

    filtered.sort(
        key=lambda x: (
            -int(x["Correct"]),
            -float(x["Percentage"]),
            float(x["Time Taken (sec)"])
        )
    )

    return filtered[:3]

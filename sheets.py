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

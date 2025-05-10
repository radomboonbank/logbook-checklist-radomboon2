import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Load credentials from Streamlit secrets
creds_dict = dict(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
credentials = Credentials.from_service_account_info(creds_dict)

# Authorize and connect to the sheet
client = gspread.authorize(credentials)
SHEET_ID = "1o5GoEyZeH5PQ1I6HlOQlpmMXAkF7OYLnWiv-wyHkKE"
SHEET_NAME = "checklist_records"
sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)

# Example: Append test row
sheet.append_row(["ทดสอบ", "2025-05-10", "OK"])
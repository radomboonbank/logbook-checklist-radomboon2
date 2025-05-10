
import streamlit as st
import json
import gspread
from google.oauth2.service_account import Credentials

# Load credentials from Streamlit secrets
creds_dict = json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
credentials = Credentials.from_service_account_info(creds_dict)

# Connect to Google Sheets
client = gspread.authorize(credentials)
SHEET_ID = "1o5GoEyZeH5PQ1I6Hl0IQpImMXAkF7OYLnWVi-wyHkKE"
SHEET_NAME = "checklist_records"

# Access the sheet
sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
st.success("Connected to Google Sheets successfully!")

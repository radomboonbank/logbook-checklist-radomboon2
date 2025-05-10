
import streamlit as st
import json
import gspread
from google.oauth2.service_account import Credentials

# Load credentials
creds_dict = json.loads(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
credentials = Credentials.from_service_account_info(creds_dict)

# Connect to Google Sheet
client = gspread.authorize(credentials)
SHEET_ID = "10o5GEyZeH5PQ1I6HlOQlpmMXAkF7OYLnWiV-wyHkKE"
SHEET_NAME = "checklist_records"

sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
data = sheet.get_all_records()

# Display records
st.title("🔍 Logbook Records")
st.write(data)

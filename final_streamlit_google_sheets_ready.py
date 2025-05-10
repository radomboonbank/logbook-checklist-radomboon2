import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# โหลด credentials โดยไม่ต้อง json.loads()
creds_dict = dict(st.secrets["GOOGLE_SERVICE_ACCOUNT"])
credentials = Credentials.from_service_account_info(creds_dict)

# ใช้งาน gspread
client = gspread.authorize(credentials)

# Example: ดึงข้อมูลจาก Google Sheets
SHEET_ID = "1o5GoEyZeH5PQ1I6H0IQpImiMXAkF7OYLnWiV-wyHkkE"
SHEET_NAME = "checklist_records"
sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)

data = sheet.get_all_records()
st.title("✅ ข้อมูลจาก Google Sheets")
st.write(data)
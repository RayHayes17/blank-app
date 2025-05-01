import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import gspread
from gspread_pandas import Client
import json

# Load service account (for local dev only — replace with st.secrets in deployment)
with open("service_account.json") as f:
    creds = json.load(f)
client = Client(credentials=creds)
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1nLT9KPSZYrQY_disCq7P5vRPGF4PHdorLNXpKZ5424Q/edit")
worksheet = spreadsheet.worksheet("Keyword Rank Tracking")
df = pd.DataFrame(worksheet.get_all_records())

# UI
st.set_page_config(page_title="SEO Dashboard", layout="wide")
with st.sidebar:
    selected = option_menu("SEO Dashboard", [
        "Overview", "Keyword Rankings", "Competitor Insights",
        "Local SEO", "Snippets", "Content Decay",
        "Reports", "Link Building"
    ])

st.title("SEO Automation Dashboard")

if selected == "Keyword Rankings":
    st.subheader("📈 Keyword Rank Tracking")
    st.dataframe(df)
else:
    st.info(f"{selected} page is under construction.")

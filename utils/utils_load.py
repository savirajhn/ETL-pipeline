import pandas as pd
import gspread
from gspread_dataframe import set_with_dataframe
from google.oauth2.service_account import Credentials

creds = Credentials.from_service_account_file("service_account.json")
client = gspread.authorize(creds)
def save_to_csv(df, filename='products.csv'):
    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan ke CSV: {e}")

def save_to_google_sheets(df, json_keyfile='projectetl-460308-c6f2aca6f555.json', sheet_url='https://docs.google.com/spreadsheets/d/1S4S_eH_7HNQ-Su2evTFauJYBA1KnZoSgL6Ii_yqPym8/edit?usp=sharing'):
    try:
        gc = gspread.service_account(filename=json_keyfile)
        sh = gc.open_by_url(sheet_url)
        worksheet = sh.sheet1
        worksheet.clear()
        set_with_dataframe(worksheet, df)
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan ke Google Sheets: {e}")

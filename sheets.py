import gspread
from oauth2client.service_account import ServiceAccountCredentials

class Sheets:
    def __init__(self):
        self.scope =["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
        self.creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", self.scope)
        self.client = gspread.authorize(self.creds)
        self.sheet = self.client.open("Live Data").sheet1

    def add_row(self, row):
        self.sheet.insert_row(row, 2)
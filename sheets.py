import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

# source Video: https://www.youtube.com/watch?v=cnPlKLEGR7E

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("quickstart").sheet1

data = sheet.get_all_records()

row = sheet.row_values(2)
col = sheet.col_values(3)

insertRow = ["hello", 5, "red", "blue"]
sheet.insert_row(insertRow, 25)

numRows = sheet.row_count

pprint(len(data))

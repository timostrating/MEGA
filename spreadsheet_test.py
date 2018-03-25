import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client-secret.json', scope)  # <-- this file should never be on github
client = gspread.authorize(creds)

sheet = client.open('2018').worksheet("test")

pp = pprint.PrettyPrinter()

result = sheet.row_values(6)

pp.pprint(result)

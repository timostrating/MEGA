from lxml import html
import requests


page = requests.get('http://localhost/MEGA/1.html')
tree = html.fromstring(page.content)




import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client-secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('2018').worksheet("test")





length = int(tree.xpath("count(//table[@class='userTable']/tr)"))


for x in range(1, length):
    value = tree.xpath("//table[@class='userTable']/tr["+str(x)+"]/td[4]/a/text()")
    value = "" if (value == []) else value[0]
    sheet.update_cell(x, 2, value) 
    print value






# print tree.xpath("//table[@class='userTable']/tr[4]/td[4]/a/@href")
# print tree.xpath("//table[@class='userTable']/tr[4]/td[4]/a/text()")

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client-secret.json', scope)  # <-- this file should never be on github
client = gspread.authorize(creds)

sheet = client.open('2018').worksheet("TIME")
cell_list = sheet.get_all_values()


DAYS_TO_CONSIDER = 180
TYPES = [ "NIKS", "SLAAP", "ETEN", "FAMILIE / VRIENDEN EN SOCIALE DINGEN", "VERVOER (AUTO / BUS / TREIN)", "VERVOER (FIETS / LOPEN / GRASMAAIEN)", "MET HARDWARE BEZIG", "OP MIJN TELEFOON", "HYGIENE", "GAMEN", "WERK", "PRODUCTIEF", "LEREN VOOR SCHOOL", "AANWEZIG BIJ LESSEN OP HET HANZE", "NAAR COLLEGES VAN DE UNIVERSITEIT"]

def get_day(day):
    return cell_list[day][2:50]

def countHours(search_var):
    sum, sum_weekend, sum_weekday = [0,0,0]
    for i in range(DAYS_TO_CONSIDER):
        for j in get_day(i):
            if int(j) == search_var:
                sum += 1
                if (i % 7 < 5):
                    sum_weekday += 1
                else:
                    sum_weekend += 1

    return "{0}, {1}%, {2}, {3}, {4}".format(sum / float(2), 
        round(sum / float(DAYS_TO_CONSIDER * 48), 3) * 100,
        '{0:2.0f}:{1:02.0f}'.format(*divmod((sum / float(2)) / float(DAYS_TO_CONSIDER) * 60, 60)),
        '{0:2.0f}:{1:02.0f}'.format(*divmod((sum_weekday / float(2)) / float(DAYS_TO_CONSIDER/float(7)*5) * 60, 60)),
        '{0:2.0f}:{1:02.0f}'.format(*divmod((sum_weekend / float(2)) / float(DAYS_TO_CONSIDER/float(7)*2) * 60, 60))) 


for i in range(len(TYPES)):
    print TYPES[i]+", "+countHours(i)

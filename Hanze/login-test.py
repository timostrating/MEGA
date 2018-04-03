# POST https://www.hanze.nl/my.policy HTTP/1.1
# Host: www.hanze.nl
# Connection: keep-alive
# Content-Length: 83
# Cache-Control: max-age=0
# Origin: https://www.hanze.nl
# Upgrade-Insecure-Requests: 1
# Content-Type: application/x-www-form-urlencoded
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# DNT: 1
# Referer: https://www.hanze.nl/my.policy
# Accept-Encoding: gzip, deflate, br
# Accept-Language: nl-NL,nl;q=0.9,en-US;q=0.8,en;q=0.7
# Cookie: cookie=!YcuExM8XsRhUJipYCQY2UAOdocKUiXBBo6ZgKCsa61y8I1bfeOgFOh4NyPoao50bD9svUMWKFdmV9X0=; _ga=GA1.2.922098361.1522661986; _gid=GA1.2.320237470.1522661986; F5_ST=1z1z1z1522662575z604800; LastMRH_Session=2b879be0; MRHSession=38e2e86894ac142a1f90d10d2b879be0; MRHSession_SP=38e2e86894ac142a1f90d10d2b879be0; TIN=278000
# 
# username=368678&password=%231009TS%23%23Hanze2&security_level=public&vhost=standard



# https://www.hanze.nl/assets/instituut-voor-communicatie-media-it/Documents/Hanze-PL-ST/Tentamenrooster/2017-2018%20P3%20wk%207-16%20Tentamens-Exams.xlsx



import requests
from lxml import html
from bs4 import BeautifulSoup

payload = {
    'username' : '_____',
    'password' : '_____',
    'security_level' : 'public',
    'vhost' : 'standard'
}

session_requests = requests.session()

login_url = "https://www.hanze.nl/my.policy"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
# authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]



# result = session_requests.post(
# 	login_url, 
# 	data = payload, 
# 	headers = dict(referer=login_url)
# )

# url = 'https://www.hanze.nl/assets/instituut-voor-communicatie-media-it/Documents/Hanze-PL-ST/Tentamenrooster/2017-2018%20P3%20wk%207-16%20Tentamens-Exams.xlsx'
# result = session_requests.get(
# 	url, 
# 	headers = dict(referer = url)
# )

# tree = html.fromstring(result.content)
# # bucket_names = tree.xpath("//ul[@class='icons-menu']/li/a/span//text()")

print(result)
print(str(tree))
print(result.content)
# print(bucket_names)
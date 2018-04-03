import urllib2

downloadurl = "https://www.hanze.nl/assets/instituut-voor-communicatie-media-it/Documents/Hanze-PL-ST/Tentamenrooster/2017-2018%20P3%20wk%207-16%20Tentamens-Exams.xlsx"
print downloadurl

opener = urllib2.build_opener()
opener.addheaders.append(('Cookie', 'WSS_KeepSessionAuthenticated={a7108d7e-2299-4b1b-98e5-ad279ed16807}'))
f = opener.open(downloadurl)
with open('test.xlsx','wb') as output:
  output.write(f.read())


print "jhee"
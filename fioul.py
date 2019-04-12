import requests
import csv
import datetime
from bs4 import BeautifulSoup

URL = "https://www.fioulreduc.com/prix-fioul"
fname = "prix_fioul.csv"
result = requests.get(URL)
c = result.content
soup = BeautifulSoup(c,"html.parser")
date_temp = datetime.datetime.now()
date = str(date_temp).split(" ")[0]
texte = soup.find_all('p',attrs={"class":"price-tracking-information"})
prixpour1000 = str(texte).split("<strong>")[2].split("euros")[0]
prix = float(prixpour1000) / 1000
file = open(fname,'a')
try:
	writer = csv.writer(file)
	writer.writerow( (date,prix) )
finally:
	file.close()

import requests
from bs4 import BeautifulSoap

# For instance, consider the following website for web-scrapping: "www.magicbricks.com"
response = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=New-Delhi")


soup = BeautifulSoap(response.content, "html.parser")


cards = soup.find_all("div", attrs = {"class":"m-srp-card__container"})


for card in cards:
	price = card.find("div", attrs = {"class":"m-srp-card__price"})


	title = card.find("span", attrs = {"class":"m-srp-card__title__bhk"})


	summary = card.find("div", attrs = {"class": "m-srp-card__summary__item"})


	data = "{} {} {}".format(title.text.strip("\n"),price.text,summary.text)
	print(data)
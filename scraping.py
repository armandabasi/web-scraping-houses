import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.funda.nl/koop/provincie-friesland/3-dagen/"

response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, "lxml")

houses = soup.find("main")

print(houses)

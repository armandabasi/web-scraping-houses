import json

from selenium import webdriver
from bs4 import BeautifulSoup

START_URL = "https://www.funda.nl"
BASE_URL = "https://www.funda.nl/koop/provincie-friesland/3-dagen/"


def find_pages(url):
    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.select("html body main form div div nav div div a")
    urls = []
    for a in pages:
        url = a["href"]
        urls.append(url)
    driver.quit()
    return urls


def find_hose(url):
    driver = webdriver.Chrome()

    driver.get(url)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    houses = soup.select(
        "main[id=content] form[method=POST] ol[class=search-results] li.search-result, li.search-result-promo")
    houses_storage_for_page = []

    for a in houses:
        street = a.find("div", class_="search-result__header-title-col").find("h2").text.strip()
        zip_code = a.find("div", class_="search-result__header-title-col").find("h4").text.strip()
        url_house = a.find("div", class_="search-result__header-title-col").find("a")["href"]

        houses_storage_for_page.append({
            "street": street,
            "zip code": zip_code,
            "url hose": url_house
        })
    driver.quit()
    return houses_storage_for_page


if __name__ == '__main__':
    houses_storage = []
    urls = find_pages(BASE_URL)
    for url in urls:
        a = find_hose(START_URL + url)
        houses_storage.append(a)

    with open("data.json", "w", encoding="utf-8") as fd:
        json.dump(houses_storage, fd, ensure_ascii=False)


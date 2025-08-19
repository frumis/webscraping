.env (stwórz plik w folderze projektu):

BASE_URL=https://fundusze.ngo.pl/aktualne
MAX_PAGES=3


scraper.py:

import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import time

# wczytanie konfiguracji
load_dotenv()
BASE_URL = os.getenv("BASE_URL")
MAX_PAGES = int(os.getenv("MAX_PAGES", 1))

headers = {"User-Agent": "Mozilla/5.0 (MyScraper/1.0)"}

for page in range(1, MAX_PAGES + 1):
    url = f"{BASE_URL}?page={page}"
    print(f"Pobieram stronę: {url}")

    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "lxml")

    cards = soup.select("article")
    if not cards:
        print("Brak ogłoszeń – koniec stron.")
        break

    print(f"Znaleziono {len(cards)} ogłoszeń na stronie {page}")
    time.sleep(2)  # grzeczny scraping
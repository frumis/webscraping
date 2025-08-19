import requests
from bs4 import BeautifulSoup

url = "https://fundusze.ngo.pl/aktualne"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

cards = soup.select("li")

for card in cards:
    title = card.select_one("h4 a")  # link w nagłówku h4
    if title:
        print("Tytuł:", title.get_text(strip=True))
        print("Link:", title.get("href"))
        print("-" * 50)
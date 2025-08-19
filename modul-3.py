import requests
from bs4 import BeautifulSoup

url = "https://fundusze.ngo.pl/aktualne"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# znajdź wszystkie linki w nagłówkach h2
headings = soup.select("h2")

for h in headings:
    print("Nagłówek:", h.get_text(strip=True))

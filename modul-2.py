import requests
from bs4 import BeautifulSoup

url = "https://fundusze.ngo.pl/aktualne"
response = requests.get(url)

# zamieniamy HTML na obiekt Soup
soup = BeautifulSoup(response.text, "lxml")

# drukujemy tytuł strony (znacznik <title>)
print("Tytuł strony:", soup.title.get_text())
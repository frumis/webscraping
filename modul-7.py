import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MyScraper/1.0; +https://example.com/bot-info)"
}

def fetch(url, retries=3, delay=2):
    for attempt in range(retries):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Błąd {response.status_code}, próba {attempt+1}")
        except requests.exceptions.RequestException as e:
            print(f"Błąd połączenia: {e}, próba {attempt+1}")
        time.sleep(delay)
    return None

# test
html = fetch("https://fundusze.ngo.pl/aktualne")
if html:
    print("Strona pobrana OK")
else:
    print("Nie udało się pobrać strony")

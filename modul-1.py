import requests

url = "https://fundusze.ngo.pl/aktualne"
response = requests.get(url)

print(response.status_code)
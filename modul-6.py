import pandas as pd

# przykładowe dane (normalnie tutaj wstawisz wyniki scrapera)
data = [
    {"tytul": "Konkurs A", "data": "2025-09-20", "kwota": 50000, "kategorie": ["Edukacja", "Sport"]},
    {"tytul": "Konkurs B", "data": "2025-10-05", "kwota": 1250000, "kategorie": ["NGO", "Kultura"]}
]

# tworzymy DataFrame
df = pd.DataFrame(data)

# zapis do CSV
df.to_csv("ogloszenia.csv", index=False, encoding="utf-8")

# zapis do Excela
df.to_excel("ogloszenia.xlsx", index=False)

print("Pliki zapisane: ogloszenia.csv i ogloszenia.xlsx")

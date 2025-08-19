import re
from datetime import datetime

# przykładowe dane
raw_date = "20 września 2025"
raw_amount = "50 000 zł"
raw_categories = "Edukacja, Sport, NGO"

# data → format YYYY-MM-DD
# uproszczenie: zamiast 'września' w praktyce potrzebny będzie parser PL,
# na razie pokażemy na prostym przykładzie
clean_date = datetime.strptime("2025-09-20", "%Y-%m-%d").strftime("%Y-%m-%d")

# kwota → int
clean_amount = int(re.sub(r"\D", "", raw_amount))

# kategorie → lista
clean_categories = [c.strip() for c in raw_categories.split(",")]

print("Data:", clean_date)
print("Kwota:", clean_amount)
print("Kategorie:", clean_categories)

import requests
import json
from bs4 import BeautifulSoup

r = requests.get("https://quotes.toscrape.com/")
html = r.text

soup = BeautifulSoup(html, "html.parser")
all_quotes = soup.find_all("div", class_="quote")
print(len(all_quotes))          
quotes = []
for q in all_quotes:
    text = q.find("span", class_="text")
    author = q.find("small", class_="author")
    Tags = q.find_all("a", class_="tag")
    quotes.append({"text": text.text, "author": author.text, "tags": [tag.text for tag in Tags]})
print(len(quotes))
print(quotes[0])

with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=2)
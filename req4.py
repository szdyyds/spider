import requests
import json
from bs4 import BeautifulSoup

quotes = []
for page in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{page}/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    all_quotes = soup.find_all("div", class_="quote")
    for q in all_quotes:
        text = q.find("span", class_="text").text
        author = q.find("small", class_="author").text
        tags = [tag.text for tag in q.find_all("a", class_="tag")]
        quotes.append({"text": text, "author": author, "tags": tags})
print(len(quotes))   
with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=2)
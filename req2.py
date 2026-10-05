import requests
from bs4 import BeautifulSoup

r = requests.get("https://quotes.toscrape.com/")
html = r.text

soup = BeautifulSoup(html, "html.parser")
all_quotes = soup.find_all("div", class_="quote")
print(len(all_quotes))          

q = all_quotes[0]
text = q.find("span", class_="text")
author = q.find("small", class_="author")
Tags = q.find_all("a", class_="tag")

print(text.text)
print(author.text)

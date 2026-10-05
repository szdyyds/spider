import requests

r = requests.get("https://example.com")
print(r.status_code)
print(r.text)
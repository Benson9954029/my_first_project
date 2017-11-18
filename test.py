import requests
from bs4 import BeautifulSoup
response = requests.get("https://en.wikipedia.org/wiki/Philosophy")
html = response.text
soup = BeautifulSoup(html,'html.parser')
print(soup.p.find_all('a'))
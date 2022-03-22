import requests
from bs4 import BeautifulSoup

URL = "https://www.mobile01.com"
r1 = requests.get(URL)
# print(r1.content)
soup1 = BeautifulSoup(r1.content, "html.parser")
print(type(soup1), soup1.title)
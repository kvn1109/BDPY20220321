import requests
from bs4 import BeautifulSoup

URL = "https://www.uuu.com.tw"
r1 = requests.get(URL)
# print(r1.content)
soup1 = BeautifulSoup(r1.content, "html.parser")
print(type(soup1), soup1.title)
promotions = soup1.find('div',{'id':'MianBanner'})
print(len(promotions))
# for p in promotions:
#     print(type(p),p)
links = promotions.find_all("a")
print(len(links))
for l in links:
    print(l.text)
    print(l.get("href"))
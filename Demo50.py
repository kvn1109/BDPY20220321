from Demo48 import BASE_URL, url2, url1
import random
import requests

if __name__ == '__main__':
    p1 = {"3":"新增的資料", "0":"new data..."}
    r1 = requests.patch(url1, json=p1)
    print(r1.status_code, r1.json())
    p2 = {'instructor':"Meng-Hang Ho",
          "level":'intermediate'}
    r2 = requests.patch(url2, json=p2)
    print(r2.status_code, r2.json())
    urlp3 = BASE_URL%("demo48_1/6")
    p3 = {"3":'kaohsiung'}
    r3 = requests.patch(urlp3, json=p3)
    print(r3.status_code, r3.json())
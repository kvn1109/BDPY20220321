from Demo48 import BASE_URL, url2, url1
import random
import requests
from pprint import pprint

if __name__ == '__main__':
    rootUrl = BASE_URL%""
    print(rootUrl)
    r1 = requests.get(rootUrl)
    print(type(r1.json()))
    responseObject = r1.json()
    print(responseObject.keys())
    for k,v in responseObject.items():
        print(f"key={k},value={v}")
    r2 = requests.get(url1)
    pprint(r2.json())
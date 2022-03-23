from Demo48 import BASE_URL, url2, url1
import random
import requests
import time
from pprint import pprint

if __name__ == '__main__':
    rootUrl = BASE_URL%""
    print(rootUrl)
    r1 = requests.get(rootUrl)
    print(r1.json().keys())
    for subUrl in r1.json().keys():
        time.sleep(2)
        u = BASE_URL%(subUrl)
        r1 = requests.delete(u)
        print(r1.status_code)
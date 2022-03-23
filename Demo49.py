from Demo48 import BASE_URL
import random
import requests


url3 = BASE_URL % ("demo49_post")

stores = ['7-11', 'fami', 'OK', 'hi-life', 'daiso']

if __name__ == '__main__':
    for _ in range(10):
        order = {"store": random.choice(stores), "quantity": random.randint(5, 10)}
        r3 = requests.post(url3, json=order)
        print(r3.status_code, r3.json())
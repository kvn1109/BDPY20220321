import requests
import time

# https://bdpydemo-5487e-default-rtdb.firebaseio.com/
# BASE_URL = "https://YOUR_URL.firebaseio.com/%s.json"
# Google提供的線上即時資料庫(nonSQL)
BASE_URL = "https://bdpydemo-5487e-default-rtdb.firebaseio.com/%s.json"

url1 = BASE_URL % "demo48_1"
url2 = BASE_URL % "demo48_2"
if __name__ == '__main__':
    time.sleep(2)
    print(url1)
    r1 = requests.put(url1, json=[1, 2, 3, None, "4", 5, ['taipei', 'hsinchu', 'taichung']])
    print(r1.status_code, r1.json())
    r2 = requests.put(url2, json={"name": "BDPY",
                                  "instructor": "Kevin Lin",
                                  "location": "台北",
                                  "occur": ['Mon', "Tue", "Wed", 'Thr', "Fri"]})
import requests
# https://bdpydemo-5487e-default-rtdb.firebaseio.com/
# BASE_URL = "https://YOUR_URL.firebaseio.com/%s.json"
BASE_URL = "https://bdpydemo-5487e-default-rtdb.firebaseio.com/%s.json"

url1 = BASE_URL % "demo48_1"
print(url1)
r1 = requests.put(url1, json=[1, 2, 3, "4", 5])
print(r1.status_code, r1.json())

import requests

# https://chrome.google.com/webstore/detail/json-viewer/gbmdgpbipfallnflgajpaliibnhdgobh?hl=zh-TW
URL = "https://bugzilla.mozilla.org/rest/bug/35"
r1 = requests.get(URL)
print(type(r1.status_code), r1.status_code)
print(r1.content)
print(type(r1.json()))
firstBug = r1.json()['bugs'][0]
for k, v in firstBug.items():
    print(f"key={k},value={v}")
print(firstBug["assigned_to_detail"]["name"])
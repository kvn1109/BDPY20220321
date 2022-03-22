import json

l1 = [1, 2, "3", "hello world", "中文", None]
s1 = json.dumps(l1)
print(s1)
d1 = {'name': 'poop', 'instructor': 'mark'}
s2 = json.dumps(d1)
print(s2)

v1 = json.loads(s1)
print(type(v1), v1)
v2 = json.loads(s2)
print(type(v2), v2)

l2 = [d1, d1, d1]
print(json.dumps(l2))
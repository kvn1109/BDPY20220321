FILE1 = "./data/Python_Introduction"
FILE2 = "./data/CLONE1"
FILE3 = "./data/CLONE2"
f1 = open(FILE1, encoding="utf-8")
d1 = f1.read()
f1.close()

print(type(f1), type(d1))
print(d1)
with open(FILE1, encoding="UTF-8") as f2:
    d2 = f2.read()

print(type(f2), type(d2))
print(d2)

f3 = open(FILE2, 'w', encoding="utf-8")
f3.write(d1)
f3.close()

with open(FILE3, 'w', encoding="UTF-8") as f4:
    f4.write(d2)
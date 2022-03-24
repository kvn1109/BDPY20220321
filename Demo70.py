def demo70():
    x = 123
    y = 45
    z = 67
    y = yield x
    yield y + z

fp1 = demo70()
print(next(fp1))
print(fp1.send(100))
#print(next(fp1))
fp2 = demo70()
print(next(fp2))
print(fp2.send(200))
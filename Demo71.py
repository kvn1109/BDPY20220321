def function71():
    a = 1
    for i in range(10):
        a += 1
        yield a
        pass
    pass
f1 = function71()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
f2 = function71()
for x in f2:
    print(x)
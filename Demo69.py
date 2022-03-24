def demo69():
    a = 1
    b = 2
    yield a
    a += b
    yield a

print(type(demo69), type(demo69()))
print(demo69)
print(demo69())
print(next(demo69()))
print(next(demo69()))
print(next(demo69()))
fp1 = demo69()
print(next(fp1), next(fp1))
#print(next(fp1))
fp2 = demo69()
print(next(fp2), next(fp2))
fp3 = demo69()
print([x for x in fp3])
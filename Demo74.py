import pandas as pd

d1 = {'poop': 35, 'bdpy': 35, 'andbiz': 28, 'testit': 14}
print(type(d1))
pd1 = pd.Series(d1)
print(type(pd1))
print(d1.keys())
print(pd1.index)
print(d1.values())
print(pd1.values)
print('poop' in d1, 'poop' in pd1)
print(d1['poop'], pd1['poop'])

l1 = ['andbiz', 'testit', 'poop', 'bdpy']
pd2 = pd.Series(d1, index=l1)
print(pd2)
l2 = ['andbiz2', 'testit', 'andbiz3', 'poop', 'bdpy']
pd3 = pd.Series(d1, index=l2)
print(pd3)
print(pd.isna(pd3))
print(pd3[pd.isna(pd3)])
print(pd.isnull(pd3))
print(pd3.isna())
print(pd3.isnull())

d2 = {'poop': 'Mark', 'bdpy': None, 'andbiz2': None, 'testit': "Frank"}
pd4 = pd.Series(d2, index=l2)
print(pd4)
print(pd4.isna())
print(pd4.isnull())
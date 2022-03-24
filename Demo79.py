import pandas as pd
import numpy as np

l1 = ['p', 'q', 'r', 's', 't']
s1 = pd.Series(range(5), index=l1)
print(s1)
print(s1.index)
index1 = pd.Index(['C', 'D', 'E', 'F', 'G', 'H'], dtype='object')
print(type(index1), index1)
print(l1[2:], l1[:2])
print(index1[2:], index1[:2])

i1 = pd.Index(np.arange(4))
i2 = list(np.arange(4))
data = ['Nangang', 'Taipei', 'Banqiao','Taoyuan']
pd1 = pd.Series(data, index=i1)
print(pd1)
pd2 = pd.Series(data, index=i2)
print(pd2)
print(2 in i1, 2 in i2)
i3 = pd.Index(['Taipei','Taipei','Taipei','Taoyuan'])
pd3 = pd.Series(data, index=i3)
print(pd3)
print(pd3['Taipei'])
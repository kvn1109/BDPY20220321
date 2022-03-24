import pandas as pd

s1 = pd.Series([1000, 800, 500, 300], index=['nangang', 'taipei', 'banqiao', 'taoyuan'])
s2 = pd.Series([500, 300, 400], index=['hsinchu', 'taichung', 'tainan'])
s3 = pd.Series([2000, 1800, 350, 200], index=['nangang', 'taipei', 'banqiao', 'taoyuan'])
s4 = pd.Series([1500, 3100, 2400], index=['hsinchu', 'taichung', 'tainan'])
print(s1)
print(s2)
print(s1 + s2)
print(s1 + s3)
print(s2 + s4)
# s5 = s1.append(s2)

s5 = pd.concat((s1, s2))
s5.name = 'sold ticket'
s5.index.name = 'station'
s5.index = ['s1', 's2', 's3', 's4', 's5', 's6', 's7']
print(s5)
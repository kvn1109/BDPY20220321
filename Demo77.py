import pandas as pd

data = {'course': ['poop', 'bdpy', 'pykt', 'aiocv'],
        'year': [2018, 2017, 2019, 2020],
        'slide': [200, 250, 230, 300]}
df1 = pd.DataFrame(data)

s1 = pd.Series(['taipei', 'hsinchu', 'taichung', 'kaohsiung'], index=[0, 1, 2, 3])
df1['location'] = s1
print(df1)

d1 = pd.Series(['remote', 'local'], index=[0, 3])
print("---" * 30)
print(d1)
df1['method'] = d1
print("---" * 30)
print(df1)
df1['heavy'] = df1['slide'] > 250
print("---" * 30)
print(df1)
del df1['slide']
print("---" * 30)
print(df1)
#s2 = pd.Series([200, 250, 230, 300, 210], index=[0, 1, 2, 3, 4])
s2 = pd.Series([200, 250, 230, 300], index=[0, 1, 2, 3])
df1['slide2'] = s2
print("---" * 30)
print(df1)

#重新排序columns
df2 = df1.reindex(columns=['year', 'course', 'method', 'location', 'heavy'])
print(df2)
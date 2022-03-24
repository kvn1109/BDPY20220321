import pandas as pd

data = {'course': ['poop', 'bdpy', 'pykt', 'aiocv'],
        'year': [2018, 2017, 2019, 2020],
        'slide': [200, 250, 230, 300]}
df1 = pd.DataFrame(data)
print(type(df1))
print(df1.head(2))
df2 = pd.DataFrame(data, columns=['course', 'slide', 'year', 'instructor'])
print(df2)
df3 = pd.DataFrame(data, index=['p1', 'p2', 'p3', 'p4'],
                   columns=['course', 'slide', 'year', 'instructor'])
print(df3)
print(df3.columns)
print(df3.index)
#Ctrl+Alt+V 抽出變數
#print(type(df3[['course', 'year']]))
var1 = df3[['course', 'year']]
print(type(var1))
print(var1)
var2 = df3['year']
print(type(var2))
print(var2)
print(df3.loc['p1'])
print(df3.loc[['p1', 'p2']])
print(df2.loc[0])
print(df2.loc[[0, 1]])
print("---" * 30)
print(df3.iloc[0])
print(df3.iloc[[0, 1]])

import pandas as pd

data = {'poop': {2019: 5, 2020: 8},
        'bdpy': {2018: 5, 2019: 7, 2020: 10}}
df1 = pd.DataFrame(data)
print(df1)
df2 = df1.T  # transpose
print(df2)
df3 = pd.DataFrame(data, index=[2018, 2019, 2020, 2021])
print(df3)
print(df3.values)
print(type(df3.values))
data1 = {'poop': {2019: 5, 2020: 8},
         'bdpy': {2018: 5, 2019: 7, 2020: 'not yet'}}
df4 = pd.DataFrame(data1, index=[2018, 2019, 2020, 2021])
print(df4)
print(type(df4))
print("***", type(df4.values), type(df4.values.dtype))
print(type(df4.values[0, 0]), type(df4.values[0, 1]))
print(df4.values[0, 0], df4.values[0, 1])
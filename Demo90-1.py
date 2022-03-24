import pandas as pd
from pandas_datareader import wb

df1 = wb.download(indicator="SE.PRM.TENR",
                  country=['all'],
                  start=2002,
                  end=2016)
print(df1.shape)
print(df1.head())
df2 = df1.reset_index()
print(df2.head())
print(df2.country.unique())
tailand_df = df2[df2.country == "Thailand"]
print(tailand_df)
print(len(df2.country.unique()))

maxValue = df2.groupby(['country'])['SE.PRM.TENR'].transform(max)
print(maxValue)
index = maxValue == df2['SE.PRM.TENR']
print(index.shape)
df3 = df2[index]
print(df3.head())
print(df3.sort_values(by='SE.PRM.TENR').head(n=10))
print(df3.sort_values(by='SE.PRM.TENR', ascending=False).head(n=10))
import pandas as pd
from pandas_datareader import wb

df1 = wb.download(indicator='SE.PRM.TENR',
                  country=['FR', 'DE', 'JP', 'KR'],
                  start=2002,
                  end=2018)
print(df1)
print("---" * 30)
df2 = df1.reset_index()
print(df2)
print("***" * 30)
unique_country = df2.country.unique()
print(unique_country)
print("---" * 30)
result = pd.Index(unique_country).get_indexer(df2.country)
print(result)
print("***" * 30)
df3 = pd.DataFrame({'FR': [1, 3, 4, 1, 4], 'DE': [2, 3, 1, 1, 4], 'JP': [3, 1, 2, 3, 4]})
print(df3)
print("---" * 30)
result = df3.apply(pd.value_counts)
print(result)
print("***" * 30)
result2 = df3.apply(pd.value_counts).fillna(0)
print(result2)
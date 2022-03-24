import pandas as pd
from pandas_datareader import wb

df1 = wb.download(indicator='SE.PRM.TENR',
                  country=['FR', 'DE', 'JP', 'KR'],
                  start=2002,
                  end=2018)
print(df1)
df2 = df1.reset_index()
print(df2)
print(df2.country.unique())
mask1 = df2.country.isin(['France', 'Germany'])
print(df2[mask1])
france1 = df2[df2.country == 'France']
germany1 = df2[df2.country == 'Germany']
print(france1)
print(france1['SE.PRM.TENR'].pct_change())
print(germany1)

france1.index = france1['year']
germany1.index = germany1['year']
df1 = pd.DataFrame({'fr': france1['SE.PRM.TENR'],
                    'de': germany1['SE.PRM.TENR']})
print(df1)
print(df1['fr'].corr(df1['de']), df1['de'].corr(df1['fr']))
print(df1['fr'].cov(df1['de']))
print(df1.corr())
print(df2.country.value_counts())
print(pd.value_counts(df2.country))
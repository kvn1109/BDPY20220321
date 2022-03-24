import pandas as pd
import numpy as np

np.random.seed(555)
df1 = pd.DataFrame(np.random.randn(6, 7),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 7, 1)))
print(df1)
df1.index = df1.iloc[:, 1]
print(df1)
print(df1.sort_index())

df1.columns = df1.iloc[2, :]
print(df1)
print("---" * 30)
df2 = df1.sort_index(axis=1)
print(df2)
print("===" * 30)

df3 = pd.DataFrame(np.random.randn(6, 7),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 7, 1)))
print(df3)
print("===" * 30)
print(df3.sort_values(by=3))
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6, 7), index=list(range(0, 12, 2)),
                   columns=list(range(0, 7, 1)))
print(df1)
print("---" * 30)
func1 = lambda x: x.max() - x.min()
print(df1.apply(func1))
print("---" * 30)
print(df1.apply(func1, axis=1))
print("---" * 30)
print(df1.apply(func1, axis='columns'))
print("---" * 30)
func2 = lambda x: pd.Series([x.max(), x.min()], index=['min', 'max'])
print(df1.apply(func2))
print("---" * 30)
print(df1.apply(func2, axis=1))
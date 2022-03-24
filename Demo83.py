import pandas as pd
import numpy as np

np.random.seed(555) #固定每次的random隨機變數
df1 = pd.DataFrame(np.random.randn(6, 7),
                   index=list(range(0, 12, 2)),
                   columns=list(range(0, 7, 1)))
print(df1)
print(df1.loc[0])  #loc表示index的編號
print(df1.iloc[0]) #iloc表示index的位置
print("---" * 30)
print(df1.loc[2])
print(df1.iloc[1])
print("---" * 30)
print(df1.loc[4])
print(df1.iloc[2])
print("===" * 30)
print(df1.loc[2:]) #slice切片：表示從index=4切到最後
print("===" * 30)
print(df1.loc[:4]) #slice切片：表示從頭切到index=4
print("===" * 30)
print(df1.loc[2:4, 1:4]) #slice切片：表示??前面是切row，後面是切col

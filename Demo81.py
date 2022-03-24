import pandas as pd

dict1 = {'station': ['nangang', 'taipei', 'banqiao', 'taoyuan', 'hsinchu'],
         'order': [1, 2, 3, 4, 5],
         'backorder': [5, 4, 3, 2, 1]}

pd1 = pd.DataFrame(dict1)
print(pd1)
print("---" * 30)
print(pd1.drop(2))
print("---" * 30)
print(pd1.drop([1, 3]))
print("---" * 30)
print(pd1.drop('order', axis=1))
print("---" * 30)
print(pd1.drop(['order', 'backorder'], axis=1))
print("---" * 30)
print(pd1.drop(['order', 'backorder'], axis='columns'))
print("---" * 30)
pd1.drop([1,4],inplace=True)
print(pd1)
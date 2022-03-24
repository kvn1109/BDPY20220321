import pandas as pd
import numpy

s1 = pd.Series([20, 15, 18, 37, 25], index=['mar', 'jan', 'feb', 'may', 'apr'])
print(s1)
s2 = s1.reindex(['jan', 'feb', 'mar', 'apr', 'may', 'jun'])
print(s2)
s3 = pd.Series(['L', 'M', 'S'], index=[0, 5, 10])
print(s3)
s4 = s3.reindex(range(15), method='ffill')
print(s4)
pd5 = pd.DataFrame(numpy.arange(16).reshape(4, 4), index=[1, 2, 3, 4],
                   columns=['kotlin', 'swift', 'c++', 'java'])
print(pd5)
pd6 = pd5.reindex(columns=['objC', 'kotlin', 'swift', 'java', 'c++'])
print(pd6)
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

np.random.seed(12345)
randomSequence = pd.DataFrame(np.random.normal(1.0, 0.07, (100, 8)))
print(randomSequence.head())
# print(randomSequence.describe())
accumulates = randomSequence.cumprod()
print(accumulates.head())
accumulates.plot()
plt.show()
import numpy as np
from matplotlib import pyplot as plt

t1 = np.arange(0, 2, 0.1)

#未疊圖的語法
# plt.plot(t1, t1, "r*", t1, t1 ** 2, "g.--", t1, t1 ** 3, 'bs-', linewidth=5)
#疊圖的語法
plt.plot(t1, t1, "r-", linewidth=1)
plt.plot(t1, t1 ** 2, "g--", linewidth=3)
plt.plot(t1, t1 ** 3, "b--", linewidth=5)
plt.show()
import numpy as np
from matplotlib import pyplot as plt

#預設range是包頭不包尾
x1 = range(0, 10, 2)
print([x for x in x1])
y1 = np.arange(0, 10, 0.5)
print([y for y in y1])

t1 = np.arange(0, 2, 0.1)
print(t1)
#是包頭又包尾 np.linspace
t2 = np.linspace(0, 2, 11)
print(t2)

plt.plot(t1, t1, "r*", t1, t1 ** 2, "g.--", t1, t1 ** 3, 'bs-', linewidth=5)
plt.show()
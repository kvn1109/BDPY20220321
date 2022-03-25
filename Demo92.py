from matplotlib import pyplot as plt
import numpy as np

X = range(0, 10)
print(X)
ax = np.array(X)
print(ax)
ay = ax ** 2
print(ay)
# ro, g*-, bs--
plt.plot(ax, ay, 'bs--')
plt.title("second plot")
plt.xlabel("label x")
plt.ylabel("label y")
# xmin, xmax, ymin, ymax
plt.axis([-10, 10, -20, 100])
plt.show()
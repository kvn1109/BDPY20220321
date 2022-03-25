import matplotlib.pyplot as plt
import numpy as np
t1 = np.arange(0, 2, 0.1)
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

#未特定宣告會畫在最後一張圖表
plt.plot(np.random.randn(20).cumsum(), "r--")
#變數不會使用可以用下底線
_ = ax1.hist(np.random.randn(200), bins=20, color='c', alpha=1)
#特別宣告要在哪一個圖表畫物件
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.randn(30))
ax4 = fig.add_subplot(2, 2, 4)
plt.plot(t1, t1 ** 3, "b--", linewidth=5)
plt.show()
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm,bernoulli,binom,poisson

mu = 80
sigma = 8
# number 1000==>1000000
X = sigma * np.random.randn(1000000) + mu
num_bins = 50

n, bins, patches = plt.hist(X, num_bins, density=1, facecolor='blue')
print(n, bins, patches)
y = norm.pdf(bins, mu, sigma)
plt.plot(bins, y, 'g^--')

plt.show()
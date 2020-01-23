"""
Histograms example.
"""
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 2, 0.5
v = np.random.normal(mu,sigma,1000)
plt.hist(v,bins=50,density=1)
plt.show()
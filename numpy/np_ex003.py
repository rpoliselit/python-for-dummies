"""
Work with functions.
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
f = np.sin(x)

plt.plot(x,f)
plt.show()
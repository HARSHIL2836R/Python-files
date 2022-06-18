import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5*(np.pi), 5*(np.pi), 0.1)

y = np.sin(x)

plt.style.use('dark_background')

plt.plot(x, y)

plt.show()

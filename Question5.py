import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.1)
y = x ** 2 + 4 * x + 10

plt.plot(x, y)
plt.show()
import numpy as np

a = np.arange(0, 12)
a = a.reshape(2, 6)

a[0] = [2, 2, 4, 8, 14, 22]
a[1] = [32, 44, 58, 74, 92, 112]

print(a)

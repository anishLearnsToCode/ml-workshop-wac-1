import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


# creating linspaces
t1 = np.arange(0, 5, 0.1)
t2 = np.arange(0, 5, 0.02)

plt.subplot(2, 1, 1)
plt.plot(t1, f(t1), 'o')
plt.plot(t2, f(t2))

plt.subplot(2, 1, 2)
plt.plot(t2, np.cos(2 * np.pi * t2))

plt.show()

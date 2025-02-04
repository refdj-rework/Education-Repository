import matplotlib.pyplot as plt
import numpy as np


Fs = 20
f = 2
sample = 20
x = np.arange(sample)
y = np.sin(2 * np.pi * f * x / Fs)
plt.plot(x, y)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')
plt.show()

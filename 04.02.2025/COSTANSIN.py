import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 77 * np.pi, 0.01)

y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

plt.figure(figsize=(10, 6))

plt.plot(x, y_sin, label='y = sin(x)', color='blue', linestyle='-')

plt.plot(x, y_cos, label='y = cos(x)', color='red', linestyle='--')

plt.plot(x, y_tan, label='y = tan(x)', color='green', linestyle=':')

plt.legend()

plt.title('Графики функций sin(x), cos(x) и tan(x)')
plt.xlabel('x')
plt.ylabel('y')

plt.ylim(-2, 2)

plt.grid(True)

plt.show()

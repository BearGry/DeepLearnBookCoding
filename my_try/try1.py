import numpy as np
import matplotlib.pyplot as plt


def step_function(x):
    y = x > 0
    return y.astype(np.int)


def sigmoid(x):
    return 1/(1+np.exp(-x))


x = np.arange(-5, 5, 0.1)
y1 = step_function(x)
y2 = sigmoid(x)

plt.plot(x, y1, label='step_function', linestyle='--', color='black')
plt.plot(x, y2, label='sigmoid')
plt.xlabel('x')
plt.ylabel('y')
plt.title('contract')
plt.ylim(-0.1, 1.1)
plt.legend()
plt.show()

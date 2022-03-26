import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - (2 * (x ** 2))

# Set up x from -10 to 10 with small steps
delta_x = 0.1
x = np.arange(-2, 3, delta_x)
# Find f(x) * delta_x
fx = f(x) * delta_x
# Compute the running sum
y = fx
# Plot the graph
plt.plot(x, y)
plt.show()
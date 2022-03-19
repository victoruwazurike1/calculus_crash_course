import numpy as np
import matplotlib.pyplot as plt

# Define function f(x)
def f(x):
    return x**2

# compute f(x) = x^2 for x=-10 to x=10
x = np.linspace(-10,10,500)
y = f(x)
# Plot f(x) on left half of the figure
fig = plt.figure(figsize=(12,5))
ax = fig.add_subplot(121)
ax.plot(x, y)
ax.set_title("y=f(x)")

# f'(x) using the rate of change
delta_x = 0.0001
y1 = (f(x+delta_x) - f(x))/delta_x
# f'(x) using the rule
y2 = 2 * x
# Plot f'(x) on right half of the figure
ax = fig.add_subplot(122)
ax.plot(x, y1, c="r", alpha=0.5, label="rate")
ax.plot(x, y2, c="b", alpha=0.5, label="rule")
ax.set_title("y=f'(x)")
ax.legend()

plt.show()
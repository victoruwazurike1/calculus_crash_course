import numpy as np
import matplotlib.pyplot as plt

# Define the range for x and y
x = np.linspace(-10,10,20)
xv, yv = np.meshgrid(x, x, indexing='ij')

# Compute the gradient of f(x,y)
fx = 2*xv
fy = 2*yv

# Convert the vector (fx,fy) into size and direction
size = np.sqrt(fx**2 + fy**2)
dir_x = fx/size
dir_y = fy/size

# Plot the surface
plt.figure(figsize=(6,6))
plt.quiver(xv, yv, dir_x, dir_y, size, cmap="viridis")
plt.show()
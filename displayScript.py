# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the mesh in polar coordinates and compute corresponding Z.
#LINSPACE: (START, END, NO_of_Points)
r = np.linspace(0, np.pi, 100) #goes from 0 radians(top) to pi(bottom)
p = np.linspace(0, 2*np.pi, 100) #full rotation

# Express the mesh in the cartesian system.
#X, Y = (R*np.cos(p)), (R*np.sin(r))
radius = 3
X = radius * np.outer(np.cos(p), np.sin(r))
Y = radius * np.outer(np.sin(p), np.sin(r))
Z = radius * np.outer(np.ones(np.size(p)), np.cos(r))

# Plot the surface.
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

# Tweak the limits and add latex math labels.
graphRange = 5
xyzRange= np.linspace((-1*graphRange),graphRange, 2)
ax.set_zlim(xyzRange)
ax.set_ylim(xyzRange)
ax.set_xlim(xyzRange)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
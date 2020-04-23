# How to create a colored grid in matplotlib

import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

data = np.random.rand(10,10)*20

#create discrete colormap
cmap = colors.ListedColormap(['green','purple'])
bounds = [0,10,20]
norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots()
ax.imshow(data, cmap=cmap)

#draw gridlines
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
ax.set_xticks(np.arange(-0.5, 10, 1));
ax.set_yticks(np.arange(-0.5, 10, 1));

plt.show()

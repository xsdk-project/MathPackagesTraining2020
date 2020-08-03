# this import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import LogNorm

# prep 3d plot area
fig = plt.figure()
ax = Axes3D(fig, azim=-128, elev=43)

# define 
s = .05
p1 = np.arange(-2, 2.+s, s)
p2 = np.arange(-1, 3.+s, s)
P1, P2 = np.meshgrid(p1, p2)
F = (1.-P1)**2 + 100.*(P2-P1*P1)**2

# plot Rosenbrock surface 
ax.plot_surface(P1, P2, F, rstride=1, cstride=1, norm=LogNorm(),
                linewidth=0, edgecolor='none', cmap="viridis")
# plot optimum solution at f(1, 1) = 0
ax.plot([1.], [1.], [0.], markerfacecolor='r', markeredgecolor='r', 
        marker='o', markersize=5)

# set the axis limits
ax.set_xlim([-2, 2.0])
ax.set_ylim([-1, 3.0])
ax.set_zlim([0, 2500])

# set axis labels and save
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("2d_rosenbrock.png", bbox_inches="tight")

plt.show()
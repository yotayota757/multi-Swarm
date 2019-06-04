import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def func(X,Y):
	return 10 * 2 + (X**2 - 10 * np.cos(2*np.pi*X) + (Y**2 - 10 * np.cos(2*np.pi*Y)))


x = np.arange(-5.12,5.12, 0.1)
y = np.arange(-5.12,5.12, 0.1)

X, Y = np.meshgrid(x,y)

Z = func(X,Y)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X,Y,Z,cmap=cm.jet)
plt.show()
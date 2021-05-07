import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

x = []
y = []
z = []

for i in range(10):
    for j in range(10):
        x.append(i)
        y.append(j)
        z.append(i*j)

ax.plot(x,y,z)
plt.show()

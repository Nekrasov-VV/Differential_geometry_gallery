import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
plt.rc("text",usetex=True)
fig=plt.figure(figsize=(3.2,3))
ax = fig.add_subplot(projection='3d')
#--------------------------------------
t = np.linspace(-np.pi, np.pi, 50)
x = np.sin(t)*np.cos(t) 
y = np.sin(t)*np.sin(t)
z = np.cos(t)
ax.plot(x, y, z, linewidth=5,color="green")
#--------------------------------------
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.sin(v)*np.cos(u)
y = np.sin(v)*np.sin(u)
z = np.cos(v)
ax.plot_wireframe(x, y, z,linewidth=0.5, color="green") 
#--------------------------------------

plt.axis('off')
plt.savefig('sph_curve.pgf', bbox_inches='tight')

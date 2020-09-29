import matplotlib.pyplot as plt
from numpy import arange
from numpy import meshgrid
import seaborn as sns
plt.rc("text",usetex=True)
plt.figure(figsize=(5,3))
#--------------------------------------
delta = 0.025
xrange = arange(-5.0, 15.0, delta)
yrange = arange(-10.0, 10.0, delta)
X, Y = meshgrid(xrange,yrange)

# F is one side of the equation, G is the other
F = X**2+Y**2
G = 8*X
plt.contour(X, Y, (F - G), [0])
#--------------------------------------
F = Y**2
G = X**3/(2-X)
plt.contour(X, Y, (F - G), [0], linestyles='dashed',colors="g")
#--------------------------------------
plt.axis('off')
plt.xlim(-8,18)
plt.ylim(-9,7)
plt.savefig('2_18.pgf', bbox_inches='tight')
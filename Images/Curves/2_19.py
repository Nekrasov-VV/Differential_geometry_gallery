from pylab import *
plt.rc("text",usetex=True)
plt.figure(figsize=(5,3))
#--------------------------------------
x=linspace(-10,10,100)
y1=(x**2)/4
y2=8/(x**2+4)
plot(x,y1, color="r")
plot(x,y2, color="g")
#--------------------------------------
axis('off')
xlim(-10,10)
ylim(0,12)
savefig('2_19.pgf', bbox_inches='tight')
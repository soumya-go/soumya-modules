import numpy as np

def Func(x,y):
	return 1.0/(1.0+(x*x+y*y))


x=y=np.arange(-10,10,0.4)
X,Y=np.meshgrid(x,y)
z=np.array([Func(x,y) for x,y in zip(np.ravel(X),np.ravel(Y))])
Z=z.reshape(X.shape)
#print Z

import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.add_subplot(111,projection= '3d')
ax.plot_surface(X,Y,Z)

plt.show()

# import sympy as python sympy
from sympy import*
import numpy as np
import matplotlib.pyplot as plt
x=Symbol("x")
f=raw_input("enter function=")
F=eval(f)
y=integrate(F)
def h(x):
	return eval(str(y))
X=np.linspace(0.1,1,1000)
Y=[h(X[i]) for i in range(len(X))]
plt.plot(X,Y)
plt.show()

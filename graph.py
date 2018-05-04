
#Welcome to plot any curve\n

from math import*
def graph_plot(g,A,B):
	import matplotlib.pyplot as plt
	def f(x):
		return eval(g)
	a=A[0]
	b=A[1]
	n=1000
	h=(b-a)/float(n)
	X=[a+i*h for i in range(n)]
	Y=[f(i) for i in X]
	plt.axis=[A,B]
	plt.plot(X,Y)
	plt.show()
if __name__=='__main__':
	g=raw_input("Enter the function to plot=")
	A=input("set xrange(x0,x1)=")
	B=input("set yrange(y0,y1)=")
	graph_plot(g,A,B)

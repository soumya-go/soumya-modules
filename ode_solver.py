###  Runge-kutta 4th order method to solve a 2nd order differential equation

def Runge_kutta_2d(first_func,second_func,initial_x,initial_y,t0=0.1):
	## Function Definitions
	def f(t,x,v):
		return eval(first_func)
	def g(t,x,v):
		return eval(second_func)
	x0=initial_x; v0=initial_y	 ##Initialization
	T=[t0]; X=[x0]; V=[v0] 		 ## Defining Matrix
	h=0.01				 ## step size

	## Main Programme
	for i in range(1000):
		t=T[i]; x=X[i]; v=V[i] 

		k1=h*g(t,x,v)
		l1=h*f(t,x,v)

		k2=h*g((t+(h/2.0)),(x+(k1/2.0)),(v+(l1/2.0)))
		l2=h*f((t+(h/2.0)),(x+(k1/2.0)),(v+(l1/2.0)))

		k3=h*g((t+(h/2.0)),(x+(k2/2.0)),(v+(l2/2.0)))
		l3=h*f((t+(h/2.0)),(x+(k2/2.0)),(v+(l2/2.0)))

		k4=h*g((t+h),(x+k3),(v+l3))
		l4=h*f((t+h),(x+k3),(v+l3))


	
		x+= (k1+2*k2+2*k3+k4)/6.0
		v+= (l1+2*l2+2*l3+l4)/6.0
		t+= h
		X.append(x)
		V.append(v)
		T.append(t)
	return X,V,T

## Euler method to solve 2nd order differential equation

def Euler_2d(first_func,second_func,initial_x,initial_y,h=0.1):
	## function Definition
	def f(x):
		return eval(first_func)
	def g(v):
		return eval(second_func)

	x0=initial_x; v0=initial_y; t0=0		## Initialization
	X=[x0]; V=[v0]; T=[t0]		## Matrix definition
	h=0.1				## step size

	

	## Main programme
	for i in range(100):
		v0+= h*f(X[i])
		x0+= h*g(V[i])
		t0+= h
		V.append(v0)
		X.append(x0)
		T.append(t0)
	return X,V,T

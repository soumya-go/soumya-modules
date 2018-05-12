from math import*
def Newton_raphson(main_func,diff_func,initial_x,eps=1E-6):
	g=main_func; dg=diff_func; x0=initial_x; c=0
	def f(x):
		return eval(g)
	def df_dx(x):
		return eval(dg)
	while abs(f(x0))>eps:
		x0=x0-f(x0)/float(df_dx(x0))
		c+=1
	iterations=c; root=x0
	return root,iterations
def bisection(function,lower_limit,upper_limit,eps=1E-5):
	g=function; a=lower_limit; b=upper_limit
	print "epsilon 1E-5"
	chn=raw_input("do you want to change(y/n)?")
	if chn=="y":
		c=input("enter epsilon=")
		eps=c
	def f(x):
		return eval(g)
	f_a=f(a)
	if f_a*f(b)>0.0:
		print "error: there is not a single root in this interval"
		sys.exit(1)
	else:
		i=0
		while (b-a)>eps:
			i+=1
			m=(a+b)/2.0
			f_m=f(m)
			if f_a*f_m<=0.0:
				b=m #root in left half
			else: 
				a=m #root in right half
				f_a=f_m
	root=m; iterations=i
	return root,iterations
## Following is the test part
if __name__=="__main__":
	print """---Newton_raphson method---"""
	g=raw_input("Enter function=")
	dg=raw_input("enter the differentiated function=")
	x=input("Enter initial x=")
	print "root=%f\niterations=%g"%(Newton_raphson(g,dg,x))


	print """----Bisection Method for root finding-----"""
	g=raw_input("Enter the function=")
	a=input("Enter lower limit=")
	b=input("Enter upper limit=")
	v,i=bisection(g,a,b)
	print "root=%lf\niteration=%d"%(v,i)

from math import*
import sys
def bisection(g,a,b,eps=1E-5):
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
	return m,i
if __name__=="__main__":
	print """----Bisection Method for root finding-----"""
	g=raw_input("Enter the function=")
	a=input("Enter lower limit=")
	b=input("Enter upper limit=")
	v,i=bisection(g,a,b)
	print "root=%lf\niteration=%d"%(v,i)


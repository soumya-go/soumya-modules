
def fact(x):
	c=1
	for i in range(1,x+1):
		c=c*i
	return c

def combination(n,m):
	return fact(n)/float(fact(m)*fact(n-m))

def binomial(event,success,probability):
	n=event; x=success; p=probability
	b=(p**x)*((1-p)**(n-x))
	return combination(n,x)*b

if __name__=='__main__':
	#check for factorial
	print """-----------
	Factorial of a no.
	-----------------"""
	x=input("Enter the no.=")
	print ("%d!=%g")%(x,fact(x))

	#check for binomial
	print "Binomial distribution"
	n=input("no. of events=")
	x=input("no. of success=")
	p=input("Enter probability=")
	print binomial(n,x,p)

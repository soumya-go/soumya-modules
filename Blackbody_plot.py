from numpy import*
import matplotlib.pyplot as plt

#constant definition
h=6.626*1E-34; c=3*1E8; k=1.38*1E-23
a=(2*h*c**2); b=(h*c)/k

def blackbody_plot(Lambda_final,n=1000):

	def blackbody(T,lam):
		return (a/lam**5)*(exp(b/lam*T)-1)**(-1)
	
	T=linspace(100,400,4)
	lam=linspace(0.1,Lambda_final,n)
	F=[]
	for i in range (len(T)):
		fi=blackbody(T[i],lam)
		F.append(fi)

	plt.plot(
	lam,F[1],lam,F[2],lam,F[3] # you can use more lam, F[i] depending on your temperature list
	)
	plt.legend(["T=%g"%(T[0]),"T=%g"%(T[1]),"T=%g"%(T[2])])
	plt.xlabel("wavelength")
	plt.ylabel("spectral radiance")
	plt.show()
if __name__=="__main__":
	
	L=input("Upper value of wavelength")
	blackbody_plot(L)

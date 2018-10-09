## putting particular values in EOS file
import numpy as np,sys

fl=open(sys.argv[1],"r")
f=open("eos_189733b_H2O+CH4.dat","w+")
A=fl.readlines()

# Modified values
a_H2O="5.000000e-04"
#a_CO="6.500000e-04"
a_CH4="5.000000e-05"
a_H2="9.999450e-01" 

#earth abundances
""" a_N2="7.800000e-01"
a_O2="2.095000e-01"
a_CO2="3.600000e-04"
a_He="5.000000e-06"
a_CH4="1.700000e-06"
a_H2="5.000000e-07"
a_O3="4.000000e-08"
a_H2O="9.300000e-03" """

"""# Jupiter Abundances
a_H2="8.745000e-01"
a_He="1.242000e-01"
a_H2O="0.000000e+00"
a_CO="0.000000e+00"
a_CH4="1.000000e-04"
"""

for i in range(len(A)):
	B=A[i].split()
	# selecting element no. in list
	if i==0:
		for j in range(len(B)):
			if B[j]=="CH4":
				n_CH4=j
				print "n_CH4",n_CH4
			if B[j]=="H2":
				n_H2=j
				print "n_H2",n_H2
			if B[j]=="H2O":
				n_H2O=j
				print "n_H2O",n_H2O
			"""if B[j]=="N2":
				n_N2=j
				print "n_N2",n_N2	
			if B[j]=="O2":
				n_O2=j
				print "n_O2",n_O2
			if B[j]=="CO2":
				n_CO2=j
				print "n_CO2",n_CO2
			if B[j]=="He":
				n_He=j
				print "n_He",n_He
			if B[j]=="CO":
				n_CO=j
				print "n_CO",n_CO
			if B[j]=="O3":
				n_O3=j
				print "n_O3",n_O3"""
		f.write(A[i])
	else:
		if len(B)==1:
			f.write(B[0])
		elif len(B)>=2:
			for k in range(len(B)):
				#if k==n_N2:
				#	f.write("%s\t"%a_N2)
				#elif k==n_O2:
				#	f.write("%s\t"%a_O2)
				#if k==n_CO:
				#	f.write("%s\t"%a_CO)
				#elif k==n_CO2:
				#	f.write("%s\t"%a_CO2)
				#if k==n_He:
				#	f.write("%s\t"%a_He)
				if k==n_CH4:
					f.write("%s\t"%a_CH4)
				elif k==n_H2:
					f.write("%s\t"%a_H2)
				#elif k==n_O3:
				#	f.write("%s\t"%a_O3)
				elif k==n_H2O:
					f.write("%s\t"%a_H2O)
				else:
					f.write("%s\t"%B[k])
		f.write("\n")

fl.close()
f.close()

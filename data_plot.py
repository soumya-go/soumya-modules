"""--------------------
This programme is used for plotting the data of 
a data file using matplotlib.
Just copy this file in the same folder your data is and 
run the code as 

$ python data_plot.py data_file

You can also change the coloumns as Needed
-----------------"""

import sys
if len(sys.argv)<2:
	print "Error: Data file is not entered"
	sys.exit(1)

import matplotlib.pyplot as plt
fl=open(sys.argv[1],"r")
A=fl.readlines()
X=[]; Y=[]
c=2; d=3      #the coloumns which you want to plot
for i in A:
	B=i.split()
	X.append(float(B[c-1]))	# X represents the c-th coloumn of your data
	Y.append(float(B[d-1]))	# Y represents the d-th coloumn of your data
plt.plot(X,Y)
plt.show()
fl.close()

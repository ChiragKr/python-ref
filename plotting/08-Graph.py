__author__ = 'Chirag'

'''customizing graph (for readability)'''

import matplotlib.pyplot as plt
mySamples = []
myQuadratic1 = []
myQuadratic2 = []
myCubic = []
myExponential = []
for i in range(30):
	mySamples.append(i)
	myQuadratic1.append(i**2)
	myQuadratic2.append(-1*(i**2)+700)
	myCubic.append(i**3)
	myExponential.append(1.5**i)

# customising display
# ===========line-style============
# SYNTAX : plt.plot(x_list, y_list, style="" , label="")

plt.figure("compare 1")
plt.clf()
plt.title("QUADRATIC COMPARISION")
plt.plot(mySamples, myQuadratic1, 'ro', label="quad-1")
plt.plot(mySamples, myQuadratic2, 'b-', label="quad-2")
plt.legend(loc="upper left")

plt.figure("compare 2")
plt.clf()
plt.title("CUBIC & EXPONENTIAL")
plt.ylim(0, 30000)
plt.xlim(0, 27)
plt.plot(mySamples, myCubic, 'g^', label = "cubic")
plt.plot(mySamples, myExponential,'r--', label = "exponential")
plt.legend(loc="upper left")

plt.show()






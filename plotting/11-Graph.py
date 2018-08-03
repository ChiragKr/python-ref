__author__ = 'Chirag'

'''changing graph scale (for readability)'''

import matplotlib.pyplot as plt
mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []
for i in range(30):
	mySamples.append(i)
	myLinear.append(i)
	myQuadratic.append(i**2)
	myCubic.append(i**3)
	myExponential.append(1.5**i)

# customising display
# ==========scale==============

plt.figure("Scaling")
plt.clf()  # clearing previous window
plt.title("CUBIC & EXPONENTIAL (in log-scale)")
plt.xlabel("sample points")
plt.plot(mySamples, myCubic, 'r', label = "cubic")
plt.plot(mySamples, myExponential, 'b', label = "exponential")
plt.yscale('log')
plt.legend(loc="upper left")
plt.show()

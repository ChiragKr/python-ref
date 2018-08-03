__author__ = 'Chirag'

'''multiple windows each with one 
plotting area and one curve in it'''

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

# graphing curves (in different windows)
# (0) create new window/figure : plt.figure(fig_name)
# (1) construct                : plt.pyplot(x_list, y_list)
# (2) display                  : plt.show()

plt.figure("Linear")
plt.plot(mySamples, myLinear)
plt.figure("Quadratic")
plt.plot(mySamples, myQuadratic)
plt.figure("Cubic")
plt.plot(mySamples, myCubic)
plt.figure("Exponential")
plt.plot(mySamples, myExponential)
plt.show()

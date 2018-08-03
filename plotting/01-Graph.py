__author__ = 'Chirag'

'''using matplotlib.pyplot to plot graphs'''
'''one plotting areas. one window. many curves'''

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

# graphing curves (in same window)
# (1) construct: plt.pyplot(x_list, y_list)
# (2) display: plt.show()

plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)
plt.show()

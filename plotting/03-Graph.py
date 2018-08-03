__author__ = 'Chirag'

'''add curve to a previously drawn window'''

import matplotlib.pyplot as plt
mySamples = []
myLinear = []
myQuadratic = []
myLinear2 = []
for i in range(30):
	mySamples.append(i)
	myLinear.append(i)
	myQuadratic.append(i**2)


# add curve to an already drawn window
plt.figure("Linear")
plt.plot(mySamples, myLinear)
plt.figure("Quadratic")
plt.plot(mySamples, myQuadratic)

myLinear2 = [2*i for i in range(30)]

plt.figure("Linear") # select window
plt.plot(mySamples, myLinear2) # add graph to selected window
plt.show()

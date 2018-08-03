__author__ = 'Chirag'

'''add x-label y-label and title to graph'''

import matplotlib.pyplot as plt
mySamples = []
myLinear = []
myQuadratic = []
myQuadratic2 = []
for i in range(30):
	mySamples.append(i)
	myLinear.append(i)
	myQuadratic.append(i**2)
	myQuadratic2.append(500 + 3*(i**2))

# (0) create new window/figure : plt.figure(fig_name)
# (1) construct                : plt.pyplot(x_list, y_list)
# (2.1) x-axis label           : plt.xlabel("x unit")
# (2.2) y-axis label           : plt.ylabel("y unit")
# (3) add title                : plt.title("GRAPH ABOUT?")
# (4) display                  : plt.show()

plt.figure("Linear")  # create window
plt.plot(mySamples, myLinear)  # plot curve

# =======adding x-label and y-label=======

plt.figure("Quadratic")  # create window
plt.plot(mySamples, myQuadratic)  # plot curve
plt.xlabel("sample points")  # add x-label

plt.figure("Linear")  # select window
plt.xlabel("sample points")    # add x-label
plt.ylabel("linear function")  # add y-label

plt.figure("Quadratic")  # select window
plt.plot(mySamples, myQuadratic2)  # add to previously drawn window
plt.ylabel("Quadratic functions")  # add y-label

# ==========adding title to a plot=========

plt.figure("Linear")  # select window
plt.title("LINEAR")  # add title
plt.figure("Quadratic")  # select window
plt.title("QUADRATIC")  # add title

plt.show()

__author__ = 'Chirag'

'''change x and y axis limits (for comparing graphs)'''

import matplotlib.pyplot as plt
mySamples = []
myCubic = []
myExponential = []
for i in range(-10, 30):
	mySamples.append(i)
	myCubic.append(i**3)
	myExponential.append(1.5**i)

# (0) create new window/figure : plt.figure(fig_name)
# (1) construct                : plt.pyplot(x_list, y_list)
# (2.1) x-axis label           : plt.xlabel("x unit")
# (2.2) y-axis label           : plt.ylabel("y unit")
# (3) add title                : plt.title("GRAPH ABOUT?")
# (4.1) x-axis limit           : plt.ylim(start, end )
# (4.2) y-axis limit           : plt.ylim(start, end)
# (4) display                  : plt.show()

plt.figure("compare")  # create window
plt.clf()  # clear window (good practice)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)
plt.title("CUBIC & EXPONENTIAL")
plt.xlabel("sample points")

# =========changing limits==========
plt.ylim(-10000, 30000)
plt.xlim(-10, 27)
plt.show()

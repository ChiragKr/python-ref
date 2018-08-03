__author__ = 'Chirag'

'''multiple plotting areas within a window'''

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
# ==========sub-plot==============
# SYNTAX: plt.subplot([ROW][COL][PLOT_NUM])

plt.figure("compare 1")
plt.clf()

plt.subplot(121)  # '121' 1 row and 2 col and 1st plot
plt.ylim(0, 30000)
plt.xlim(0, 27)
plt.plot(mySamples, myCubic, 'g--', label = "cubic", linewidth=2.0)
plt.legend()

plt.subplot(122)  # '122' 1 row and 2 col and 2nd plot
plt.xlabel("sample points")
plt.ylim(0, 30000)
plt.xlim(0, 27)
plt.plot(mySamples, myExponential,'r', label = "exponential", linewidth=2.0)
plt.legend()


# customising display
# ==========sub-plot==============
# SYNTAX: plt.subplot([ROW][COL][GRAPH_NUM])

plt.figure("compare 2")
plt.clf()

plt.subplot(211)  # '211' 2 row and 1 col and 1st plot
plt.ylim(0, 30000)
plt.xlim(0, 27)
plt.plot(mySamples, myCubic, 'g--', label = "cubic", linewidth=2.0)
plt.legend()

plt.subplot(212)  # '212' 2 rows and 1 col and 2nd plot
plt.xlabel("sample points")
plt.ylim(0, 30000)
plt.xlim(0, 27)
plt.plot(mySamples, myExponential,'r', label = "exponential", linewidth=2.0)
plt.legend()
plt.show()

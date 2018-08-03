__author__ = 'Chirag'

'''customizing graph (for readability)'''

import matplotlib.pyplot as plt
mySamples = []
myCubic = []
myExponential = []
for i in range(30):
	mySamples.append(i)
	myCubic.append(i**3)
	myExponential.append(1.5**i)

# customising display
# ==========line-width==============
# SYNTAX : plt.plot(x_list, y_list, style="" , label="", linewidth=float)

plt.figure("compare")
plt.clf()
plt.title("CUBIC & EXPONENTIAL")
plt.ylim(0, 30000)
plt.xlim(0, 27)
plt.plot(mySamples, myCubic, 'g', label = "cubic", linewidth=1.0)
plt.plot(mySamples, myExponential,'r', label = "exponential", linewidth=5.0)
plt.legend()

plt.show()

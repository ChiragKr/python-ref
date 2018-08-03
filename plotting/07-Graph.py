__author__ = 'Chirag'

'''adding legend for clarity/readability'''

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

# adding labels to plots and display legend

plt.figure("compare")
plt.clf()
plt.title("CUBIC & EXPONENTIAL")
plt.ylim(0, 30000)
plt.xlim(0, 27)
plt.xlabel("sample points")

plt.plot(mySamples, myCubic, label="cubic")  # add label (shows up in legend)
plt.plot(mySamples, myExponential, label="exponential")  # add label (shows up in legend)

plt.legend(loc="upper left")  # 'loc' = 'location' (if not parameter passed, automatic.)
plt.show()

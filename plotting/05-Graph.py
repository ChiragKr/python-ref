__author__ = 'Chirag'

'''completely clear old window and redraw'''

import matplotlib.pyplot as plt
mySamples = [i for i in range(30)]
myCubic = [i**3 for i in range(30)]

# Draw on the window "Cubic"
plt.figure("Cubic")  # create
plt.plot(mySamples, myCubic)  # plot
plt.xlabel("sample points")
plt.ylabel("x**3")
plt.title("CUBIC FUNCTION")
plt.show()

# clearing window "Cubic"
plt.figure("Cubic")  # select
plt.clf()  # clear
plt.show()

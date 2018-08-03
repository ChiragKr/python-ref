__author__ = 'Chirag'

"""decide an appropriate amount of monthly deposit 
by graphing interest accumulated vs total months. 
decision based on retirement goals"""

import matplotlib.pyplot as plt


def retire(monthly, rate, terms):
	"""
	monthly = monthly deposit
	rate    = rate of interest
	terms   = number of months
	"""
	savings = [0]  # the y-values
	base = [0]  # the x-values
	m_rate = rate/12
	for i in range(terms):
		base += [i]  # month added
		savings += [savings[-1]*(1+m_rate) + monthly]  # savings in that month
	return base, savings


def displayRetireWMonthlies(monthlies, rate, terms):
	plt.figure('retireMonth')
	plt.clf()
	for monthly in monthlies:
		xvals, yvals = retire(monthly, rate, terms)
		plt.plot(xvals, yvals, label="retire:"+str(monthly))
		plt.legend(loc="upper left")


def displayRetireWRates(month, rates, terms):
	plt.figure('retireRate')
	plt.clf()
	for rate in rates:
		xvals, yvals = retire(month, rate, terms)
		plt.plot(xvals, yvals, label="retire:"+str(month)+":"+str(int(rate*100)))
		plt.legend(loc="upper left")


def displayRetireWMonthlsAndRates(monthlies, rates, terms):
	plt.figure('retireBoth')
	plt.clf()
	plt.xlim(30*12, 40*12)
	monthLabels = ['r', 'b', 'g', 'k']
	rateLabels = ['-', 'o', '--']
	for i in range(len(monthlies)):
		monthly = monthlies[i]
		monthLabel = monthLabels[i%len(monthlies)]
		for j in range(len(rates)):
			rate = rates[j]
			rateLabel = rateLabels[j%len(rates)]
			xvals, yvals = retire(monthly, rate, terms)
			plt.plot(xvals, yvals, monthLabel+rateLabel, label="retire:"+str(monthly)+":"+str(int(rate*100)))
			plt.legend(loc="upper left")


monthlies = [500, 600, 700, 800, 900, 1000, 1100]
displayRetireWMonthlies(monthlies, 0.05, 40*12)

rates = [0.03, 0.05, 0.07]
displayRetireWRates(800, rates, 40*12)

monthlies = [500, 700, 900, 1100]
displayRetireWMonthlsAndRates(monthlies, rates, 40*12)

plt.show()




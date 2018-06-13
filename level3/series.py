__author__ = 'Chirag'

class Series():
	def __init__(self, a, d, n):
		self.a = a
		self.d = d
		self.n = n

	def __str__(self):
		my_series = [self.a]
		for i in range(1,self.n):
			my_series.append(my_series[i-1] + self.d)
		return str(my_series)

s = Series(1,1,10)
print(s)

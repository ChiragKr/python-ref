__author__ = 'Chirag'

class Imputer():

	def __init__(self,missing_values="NaN", strategy = "mean", axis = 0):
		self.missing_values = missing_values
		self.strategy = strategy
		self.axis = axis

	def impute(self, lst=[]):


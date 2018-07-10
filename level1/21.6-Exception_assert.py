__author__ = 'Chirag'

""" just like raise, assert is used to raise an
AssertionError when certain conditions are not met
usually it to 'assert' inputs are of a certain kind
and if they are not. An Exception is raised"""


def avg(grades):
	assert not len(grades) == 0
	return sum(grades)/len(grades)


print(avg([14, 17, 13, 15, 18, 15]))
print(avg([]))  # throws an Exception

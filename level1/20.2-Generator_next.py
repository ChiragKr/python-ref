__author__ = 'Chirag'

def create_cubes(n):  # 1st time call, execution starts from here
	"""yields cubes from 0 to n"""
	for x in range(n): # next call. evaluation starts for here
		yield x**3
		# value evaluated after the 'yield' keyword is returned


g = create_cubes(5)  # g is a generator object
print(g)
print(next(g))  # manually calls g and prints 1st yield
print(next(g))  # g is called but execution gives 2nd yield
print(next(g))
print(next(g))
print(next(g))
# print(next(g)) error!


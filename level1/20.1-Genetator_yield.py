__author__ = 'Chirag'

# =============================================================


def create_cubes(n):
	"""returns list of cubes from 0 to n"""
	result = []
	for x in range(n):
		result.append(x**3)
	# entire 'result' list in memory (inefficient)
	return result


for x in create_cubes(10):
	print(x)
print()
# =============================================================


def create_cubes(n):  # 1st time call, execution starts from here
	"""yields cubes from 0 to n"""
	for x in range(n): # next call. evaluation starts for here
		yield x**3
		# value evaluated after the 'yield' keyword is returned


for x in create_cubes(10):
	print(x)
# =============================================================

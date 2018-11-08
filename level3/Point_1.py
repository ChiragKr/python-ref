import math

class Point(object):
	
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def __str__(self):
		return "({}, {})".format(self.x, self.y)

	def __eq__(self, B):
		if self.x == B.x and self.y == B.y:
			return True
		return False

	# def __eq__(self, B):
	# 	if Point.distance(self, B) == 0 :
	# 		return True
	# 	return False

	@staticmethod
	def distance(A, B):
		dX = math.pow(A.x - B.x, 2)
		dY = math.pow(A.y - B.y, 2)
		return math.sqrt(dX + dY)

A = Point()
B = Point(4, 3)
print(A)
print(B)
print(Point.distance(A, B))
print("A == B ? ", A == B)
C = Point(4, 3)
print("C == B ? ", C == B)
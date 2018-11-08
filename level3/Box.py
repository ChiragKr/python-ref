import math

class Box(object):

	number_of_boxes = 0

	def __init__(self, height=0, width=0, depth=0):
		self.height = height
		self.width = width
		self.depth = depth
		Box.number_of_boxes += 1

	def __str__(self):
		return "{0:1.3f}*{1:1.3f}*{2:1.3f}".format(self.height, self.width, self.depth)

	def __eq__(self, B2):
		return abs(self.volume() - B2.volume()) < 10 ** -6
		# return self.volume() == B2.volume() # might give some problems

	# def __eq__(self, B2):
	# 	if self.height != B2.height
	# 		return False
	# 	if self.width != B2.width
	# 		return False
	# 	if self.depth != B2.depth
	# 		return False
	# 	return True

	def volume(self):
		return self.height*self.width*self.depth

	def reshape_to_cube(self):
		side = math.pow(self.volume(), 1/3)
		self.height = side
		self.width = side
		self.depth = side


b1 = Box()
print("number_of_boxes = ", Box.number_of_boxes)
b2 = Box(5, 7, 2)
print("number_of_boxes = ", Box.number_of_boxes)
print("b1 = ",b1)
print("b2 = ",b2)

print("Volume of b1 = ", b1.volume())
print("Volume of b2 = ", b2.volume())

b3 = Box(7, 2, 5)
b4 = Box(5, 7, 2)
print("number_of_boxes = ", Box.number_of_boxes)
print("b3 = ",b3)
print("b4 = ",b4)

print("b2 == b1 ? ", b2 == b1)
print("b2 == b2 ? ", b2 == b2)
print("b2 == b3 ? ", b2 == b3)
print("b2 == b4 ? ", b2 == b4)

print("reshaping b3 into a cube")
b3.reshape_to_cube()
print("After reshaping : b3 = ", b3)
print("b2 == b3 ? ", b2 == b3)
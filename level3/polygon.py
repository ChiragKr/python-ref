__author__ = 'Chirag'

import math
import matplotlib.pyplot as plt

class Polygon():
	def __init__(self,side_length, num_of_sides):
		self.num_of_sides = num_of_sides
		self.side_length = side_length

	def get_area(self):
		theta = ((self.num_of_sides-2)*math.pi)/(2*self.num_of_sides)
		area = ((1/4)*pow(self.side_length,2)*math.tan(theta))*self.num_of_sides
		return area

	def get_perimeter(self):
		return self.num_of_sides*self.side_length

P = Polygon(42,5)
area = P.get_area()
peri = P.get_perimeter()

print("Side Length : {}".format(P.side_length))
print("Total Sides : %d"%P.num_of_sides)
print(f"Area        : {area:5.3f}")
print(f"Perimeter   : {peri:5.3f}")

length_vals = list(range(1,30))
area_vals = list(map(lambda side : Polygon(side,10).get_area(), length_vals))
pairs = list(zip(length_vals,area_vals))
for item in pairs:
	print(item)

plt.scatter(*zip(*pairs))
plt.show()

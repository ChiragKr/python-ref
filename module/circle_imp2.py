__author__ = 'Chirag'

"""importing modules into another file
using the keyword 'as' for aliasing """

import module.circle as circle

pi = 3
print(pi)
print(circle.pi)
print(circle.area(3))
print(circle.circumference(3))

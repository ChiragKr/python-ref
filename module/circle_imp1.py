__author__ = 'Chirag'

"""importing modules into another file"""

import module.circle

pi = 3
print(pi)
print(module.circle.pi)
print(module.circle.area(3))
print(module.circle.circumference(3))

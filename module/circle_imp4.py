__author__ = 'Chirag'

"""importing modules into another file
using the wildcard '*' use this method only
when there is no name space collision"""


from module.circle import *

pi = 3
print(pi)
print(pi)  # cannot reference "pi" within circle.py
print(area(3))
print(circumference(3))

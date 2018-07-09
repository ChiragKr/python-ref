__author__ = 'Chirag'

"""importing a specific function from 
a modules into another file with aliasing"""

from module.circle import area as ar

pi = 3
print(pi)
print(ar(3))

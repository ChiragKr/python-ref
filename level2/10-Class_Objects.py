__author__ = 'chira'

class Dog:

    kind = 'canine'         # class variable SHARED BY ALL instances

    def __init__(self, name):
        self.name = name    # instance variable UNIQUE TO EACH instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)      # shared by all "Dog" objects
print(e.kind)      # shared by all "Dog" objects
print(d.name)      # unique to each instance of a "Dog"
print(e.name)      # unique to each instance of a "Dog"

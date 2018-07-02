__author__ = 'Chirag'
'''Difference between class variable and instance variable
and how to use a class variable '''


class Animal(object):
	def __init__(self, age):  # 'name' and 'age' are instance variables
		self.age = age
		self.name = None

	def get_age(self):
		return self.age

	def get_name(self):
		return self.name

	def set_age(self, new_age):
		self.age = new_age

	def set_name(self, new_name=""):
		self.name = new_name

	def __str__(self):
		return "animal:"+str(self.name)+":"+str(self.age)


class Rabbit(Animal):
	tag = 1  # 'tag' is a class variable. gives unique ID to each new rabbit instance

	def __init__(self, age, parent1=None, parent2=None):
		Animal.__init__(self, age)  # invoking superclass constructor
		self.parent1 = parent1  # 'parent1' is expected to an instance of Rabbit class
		self.parent2 = parent2  # 'parent2' is expected to an instance of Rabbit class
		self.rid = Rabbit.tag  # 'rid' is an instance variable. 'tag' is a class variable
		Rabbit.tag += 1  # how to refer to a class variable. <classname>.<variablename>

	def get_rid(self):
		return str(self.rid).zfill(3)

	def get_parent1(self):
		return self.parent1

	def get_parent2(self):
		return self.parent2

	def __add__(self, other):  # operator overloading. defined addition of two 'Rabbit' instances
		return Rabbit(0, self, other)  # here '+' would create a new Rabbit. ('+' = mating)

	def __eq__(self, other):  # defines when are two Rabbit instances are equals. (When they siblings)
		# we use the fact that each Rabbit has a unique 'rid' associated thanks to the class variable
		parents_same = self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid
		parents_opposite = self.parent1.rid == other.parent2.rid and self.parent1.rid == other.parent2.rid
		return parents_same or parents_opposite


peter = Rabbit(2)  # calling Rabbit.__init__() to create an instance
peter.set_name('Peter')  # method from parent class, 'Animal' used
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1, peter, hopsy)
cotton.set_name('Cottontail')

print(cotton)  # Animal.__str__(cotton) is called
print("Cottontail's parent1 = "+ cotton.get_parent1().name)
print("Cottontail's parent2 = "+ cotton.get_parent2().name)
print()

mopsy = peter + hopsy  # 'mopsy' and 'cotton' are siblings in this context
mopsy.set_name('Mopsy')

print(mopsy)
print("Mopsy's parent1 = "+ mopsy.get_parent1().name)
print("Mopsy's parent2 = "+ mopsy.get_parent2().name)
print()

print("Are mopsy and cotton siblings? Ans = "+ str(mopsy == cotton))

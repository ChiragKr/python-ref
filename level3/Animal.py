__author__ = 'Chirag'

'''Idea of Hierarchies. Idea of Inheritance'''
import random


class Animal(object):
	def __init__(self, age):
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


myAnimal = Animal(9)  # creating instance of class 'Animal'. __init__ method invoked
print(myAnimal)
myAnimal.set_name("Tofu")
print(myAnimal)


class Cat(Animal):
	# 'speak' is a new functionality specific to Cat class
	# the Animal class cannot use the 'speak' method
	def speak(self):
		print("meow")

	# '__str__' for cat-class overrides the '__str__' for animal-class
	def __str__(self):
		return "cat:"+str(self.name)+":"+str(self.age)


jelly = Cat(1)  # '__init__' of 'Animal' class invoked here
jelly.set_name('Jelly')
print(jelly.get_name())

# 'Animal' class CANNOT use methods of 'Cat' class but the
# 'Cat' class CAN use the methods of the 'Animal' class

print(jelly)  # '__str__' overridden by 'Cat' is invoked
print(Animal.__str__(jelly)) # '__str__' for 'Animal' needs explicit referencing


class Rabbit(Animal):
	def speak(self):
		print("meep")

	def __str__(self):
		return "rabbit:"+str(self.name)+":"+str(self.age)


peter = Rabbit(5)  # '__init__' from 'Animal' class invoked
jelly.speak()  # 'speak' method from 'Cat' class
peter.speak()  # 'speak' method from 'Rabbit' class
# myAnimal.speak() : AttributeError: 'Animal' object has no attribute 'speak'

# if a subclass does not have the called method, it looks for it in up in the hierarchy


class Person(Animal):
	def __init__(self, name, age):
		Animal.__init__(self, age)  # using underlying 'Animal' constructor
		Animal.set_name(self, name)  # using underlying 'Animal' method
		self.friends = []  # directly adding new data attribute

	def get_friends(self):
		return self.friends

	def add_friend(self, fname):
		if fname not in self.friends:
			self.friends.append(fname)

	def speak(self):
		print("Hello")

	def age_diff(self, other):
		diff = self.get_age() - other.get_age()
		# alternate way : self.age - other.age
		if diff > 0:
			print(self.name+" is ", diff, "years older than ", other.name)
		else:
			print(self.name+" is", -1*diff, "years younger than", other.name)

	def __str__(self):
		return "person:"+str(self.name)+":"+str(self.age)


dan = Person('Dan', 21)
john = Person('John', 35)

dan.speak()
dan.age_diff(john)
Person.age_diff(dan, john)  # alternate invocation


class Student(Person): # Student inherits from Person which in turn inherits from Animal
	def __init__(self, name, age, major=None):
		Person.__init__(self, name, age)  # using 'Person' class constructor
		self.major = major

	def change_major(self, major):
		self.major = major

	def speak(self):
		r = random.random()
		if r < 0.25:
			print("I have homework")
		elif 0.25 <= r < 0.5:
			print("I need to sleep")
		elif 0.5 <= r < 0.75:
			print("I should eat")
		else:
			print("I m watching TV")

	def __str__(self):
		return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)


fred = Student('Fred', 22, "Mathematics")
print(fred)
fred.speak()

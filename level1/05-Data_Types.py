__author__ = 'Chirag'

def print_info(x):
	print ("x = {} and it is of the type {}".format(x, type(x)))

#==============================================
#1 Integer  (built-in | primitive | numeric)
x = 5
print_info(x)

#2 Floating (built-in | primitive | numeric)
x = 3.14
print_info(x)

#3 String   (built-in | primitive | textual)
x = "Chirag"
print_info(x)

#4 Boolean  (built-in | primitive | True/False)
x = True
print_info(x)
#==============================================
#5 List     (built-in | composite | mixed)
x = ["Ben", 3.23, 22, "Tina"]
print_info(x)

#6 Tuple    (built-in | composite | mixed)
x = ("Ben", 3.23, 22, "Tina")
print_info(x)
#==============================================
#7 Dictionary (built-in | composite | mixed)
x = {"Home": "Lko", "Chirag": 20}
print_info(x)

#8 Set        (built-in | composite | mixed)
x = {3,2,4,5,4,4,4,4,5,5,5}
print_info(x)
#==============================================
#9 Object     (custom | composite | mixed)
class Person():
	def __init__(self,name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender
	def __str__(self):
		info = str({"name": self.name,
		            "age": self.age,
		            "gender" : self.gender})
		return info
x = Person("Ben",15,"M")
print_info(x)
#==============================================
# string , lists and tuples are SEQUENTIAL
# therefore we have indexing and slicing
x = "Chirag"
print(x[3]) #--> r
print(x[1:4]) #--> hir
x = [34,21,"Red"]
print(x[1]) #--> 21
x = (34,21,"Red")
print(x[2]) #--> Red
# Dictionary is like a key-value MAPPING
# Dictionary and sets are NOT SEQUENTIAL
#==============================================



__author__ = 'Chirag'

"""using the keyword 'raise' we can manually raise an
exception of a given type and python will terminate
program and display our message"""

# SYNTAX : raise <Exception_type>("descriptive string")

"""code exemplifies: default error type and custom raise"""


def input_age():
	try:
		age = int(input("Enter age   : "))
		if age < 0:
			raise ValueError("Age cannot be negative")
			# raise ValueError
		else:
			print("Inputted age = ", age)
			return age
	finally:
		pass


input_age()

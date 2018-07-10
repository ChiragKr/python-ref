__author__ = 'Chirag'

"""creating custom exceptions allows us maximum
control as we can even add parameters to our 
exception object with can be dealt with in the 
corresponding except block"""

"""
SYNTAX :

raise Exception_object
except Exception_object as e
"""

"""code exemplifies: custom error type and custom raise"""


class NegativeAge(Exception):  # creating custom exception
	def __init__(self, age):
		self.msg = "Age cannot be negative!"


class ZeroAge(Exception):  # creating custom exception
	def __init__(self):
		self.msg = "You cannot be 0 years old!"


def input_age():
	try:
		age = int(input("Enter age   : "))
		if age == 0:
			exception = ZeroAge()  # creating an zeroAge Exception object that will trigger corresponding except block
			raise exception
		elif age < 0:
			raise NegativeAge(age)  # creating an anonymous negativeAge Exception object that will trigger corresponding except block

	except NegativeAge as e:
		print(f"{age} is not a valid age")
		print(e.msg)

	except ZeroAge as e:
		print(e.msg)

	else:
		print("Inputted age = ", age)
		return age

	finally:
		print("ALWAYS EXECUTED even if try/except block has break, continue or return statements")

	print("Outside. Not executed if break, continue or return statements in them")


input_age()

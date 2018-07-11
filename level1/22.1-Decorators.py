__author__ = 'Chirag'

"""Decorators are a good use of higher order programming.
functions are said to be first class object. functions can
themselves be treated as objects and therefore can be passed 
as parameters to other functions and can be returned"""


def new_decorator(some_function):
	# the function inside another function is called a helper function
	def wrap_func():
		print("add functionality before function")
		some_function()
		print("add functionality after function")
	return wrap_func


def my_function():
	print("function that needs decoration!")


decorated_function = new_decorator(my_function)
decorated_function()

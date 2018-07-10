__author__ = 'Chirag'

try:
	a = float(input("Enter numerator   : "))
	b = float(input("Enter denominator : "))
	print("a + b = ", a + b)
	print("a / b = ", a / b)
except ValueError:
	print("Could not convert to a number")
except ZeroDivisionError:
	print("Can't divide by 0!")
else:
	print("Executed when no exception is raised in try block")
finally:
	print("ALWAYS EXECUTED even if try/except block has break, continue or return statements")

print("Outside. Not executed if break, continue or return statements in them")


__author__ = 'Chirag'

"""Error Handling allows us to write special code that is 
run when some unexpected situation is encountered rather than
simply stopping the execution like python would normally do!"""


"""code exemplifies: default error type and default raise"""


try:  # try-block : where we are expecting some exception to be raised
	a = float(input("Enter numerator   : "))
	b = float(input("Enter denominator : "))
	print("a + b = ", a + b)
	print("a / b = ", a / b)

except ValueError:  # ValueError exception handled here
	print("Could not convert to a number")

except ZeroDivisionError:  # ZeroDivisionError exception handled here
	print("Can't divide by 0!")

except:  # a "catch all" for any other kind of error exception
	print("Some bug is code!")

else:  # runs only when try-block is exception-free
	print("Executed when no exception is raised in try block")

finally:  # always executed even in presence of break, continue or return
	print("ALWAYS EXECUTED even if try/except block has break, continue or return statements")

print("Outside. Not executed if break, continue or return statements in them")


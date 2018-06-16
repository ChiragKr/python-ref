_author__ = 'Chirag'

# A Variable stores data value
# A Functions stores lines of code

# Functions help up "DRY" code (Don't Repeat Yourself)
# Otherwise we have "WET" code (Write Everything Twice)

# Functions and/or Loops help write DRY code

def func():
    print("You called func()! ")
    print("The block of code inside func() is being executed")
    x = 2.345
    print(f"value of x (a variable inside func()) is = {x}")
    print(f"sqrt(x) = {x**0.5}")
    print()

# "calling" the function 'func'
func()

# Code is Reusable
func()
func()

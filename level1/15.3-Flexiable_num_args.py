__author__ = 'Chirag'

# ======================================================================
# flexible number of arguments (*args)
'''When a function parameter starts with an asterisk (*), 
it allows for an arbitrary number of arguments, 
and the function takes them in as a TUPLE of values.'''


def add_numbers(*args): # number of arguments unknown
    print(f"args = {args}")
    print(f"type(args) = {type(args)}")
    total = 0
    for a in args:
        total += a
    print("sum = %s" % total)


add_numbers(3)
add_numbers(3, 5)
add_numbers(3, 5, 7, 21)
# ======================================================================
# flexible number of keyword arguments (*kwargs)
'''When a function parameter starts with two asterisk (**), 
it allows an arbitrary number of keyword arguments. Instead 
of creating a tuple of values, **kwargs builds a DICTIONARY 
of key/value pairs'''


def fav_fruit(**kwargs):
    print(f"kwargs = {kwargs}")
    print(f"type(kwargs) = {type(kwargs)}")
    if 'fruit' in kwargs:
        print(f"My favorite fruit is {kwargs['fruit']}")
    else:
        print("I don't like fruit!")


fav_fruit(fruit='pineapple')
fav_fruit(name="Ben")
fav_fruit(fruit='pineapple', name="Ben")
# ======================================================================

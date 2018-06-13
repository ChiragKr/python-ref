__author__ = 'chira'

# flexible number of arguments

def add_numbers(*args): # number of arguments unknown
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(3, 5)
add_numbers(3, 5, 7, 21)
__author__ = 'Chirag'

# a shorter syntax to create lists quickly
# very closely linked to set builder notation from math

lst = [x for x in 'word']
print(f"lst = [x for x in 'word'] = {lst}")
print()
lst = [x**2 for x in range(0,6)]
print(f"lst = [x**2 for x in range(0,6)] = {lst}")
print()
lst = [x for x in range(11) if x % 2 == 0]
print(f"lst = [x for x in range(11) if x % 2 == 0] = {lst}")
print()

# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit) #--> [32.0, 50.0, 68.18, 94.1]
print()

# Nested List Comprehensions
lst = [ x**2 for x in [x**2 for x in range(11)]]
print(lst) #--> [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]

__author__ = 'Chirag'
#===============================================================
# range(start, stop, step) --> list(range()) : a list
l = list(range(0,12,2))
print(f"l = list(range(0,12,2)) = {l}")
print()

# enumerate(iterable) --> list(enumerate()) : a list of tuples
s = "ABCDEF"
print(f"s = {s}")
l = list(enumerate(s))
print(f"list(enumerate(s)) = {l}")
print()

# zip(iterable_1, iterable_2) -- > list(zip()) : a list of tuples
s1 = "ABCDEF"
s2 = "UVWXYZ"
print(f"s1 = {s1}")
print(f"s2 = {s2}")
l = list(zip(s1, s2))
print(f"list(zip(s1, s2)) = {l}")
l = list(zip(s2, s1))
print(f"list(zip(s2, s1)) = {l}")
print()
#===============================================================
# 'in' keyword : checks equality for iterable
s1 = "Chirag"
print(f"s1 = {s1}")
val = 'C' in s1
print(f"val = 'C' in s1 = {val}")
val = 'c' in s1
print(f"val = 'c' in s1 = {val}")
print()

l = [35,82,52,21,32]
print(f"l = {l}")
print(f"min(l) = {min(l)}") # min(my_list) : returns minimum value in my_list
print(f"max(l) = {min(l)}")# max(my_list) : returns maximum value in my_list
print()

# random : a library to perform randomization tasks
from random import shuffle
print(f"l = {l}")
print("calling shuffle(l)...")
shuffle(l) # shuffle(my_list) --> random orders my_list
print(f"l = {l}")
print()

from random import randint
r_num = randint(10,50) # randint(int_1,int_2) --> random number between num_1 and num_2
print(f"r_num = randint(10,50) = {r_num}")
print()
#===============================================================
# input(str_prompt) --> returns input by user as a str
name = input("name = Enter your name : ");
age = input(f"age = Hello {name}! how old are you? ")
print(f"name = {name} is of type {type(name)}")
print(f"age = {age} is of type {type(age)}")

#===============================================================

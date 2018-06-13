__author__ = 'Chirag'

y = ["Tom", 2.71, 36, 36] # is a list. MUTABLE
z = ("Tom", 2.71, 36, 36) # tuple is IMMUTABLE
#==============================================
# CREATING tuples (only declaring method!)
t = ("Lara", True, 25, 3.145, True)
print(f"t = {t} \n")
#==============================================
# ACCESSING element of a tuple
x = t[2] # INDEXING
print(f"t[2] = {x} \n")
#==============================================
# METHODS for tuples
x = t.index(True)
print(f"t.index(True) = {x}") #first occurence index
x = t.count(True)
print(f"t.count(True) = {x}") #number of occurances
print()
#==============================================
# TUPLE UNPACKING
# given a list of tuples we can access invidual
# elements in a single for loop
lst = [(1,2,3),("a","b","c"),("x",4,"y")]
for a,b,c in lst:
	print(f"{a}___{b}___{c}")


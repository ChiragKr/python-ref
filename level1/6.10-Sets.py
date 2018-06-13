__author__ = 'Chirag'

x = {"Tom", 2.71, 36, 36} # is a set. REPETITION NOT ALLOWED
y = ["Tom", 2.71, 36, 36] # is a list. MUTABLE

print("x is a   SET : ", x)
print("y is a  LIST : ", y)
print()
#===========================================
# CREATE sets
s = {1,2,3,4,5}       # direct declare
print(s)
s = set()
for i in range(1,6):
	s.add(i)           # using .add() method
print(s)
s = set([x for x in range(1,6)])
print(s)   # list comprehension + conversion
print()
#===========================================
# SETS don't have order. Therefore no
# indexing access is available
list1 = [1,1,2,2,3,4,5,6,1,1]
print(f"list1 = {list1}")
s = set(list1)
print(f"s = set(list1) = {s}")
print()
#===========================================
# METHODS for sets include .intersection()
# .union() .issubset() etc.
print(f"len(s) = {len(s)}")
#===========================================

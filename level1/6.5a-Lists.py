__author__ = 'Chirag'

#=====================================================================
# set   != list. Does not support indexing
# tuple != list. Does not support mutation

x = {"Tom", 2.71, 36, 36} # is a set. REPETITION NOT ALLOWED
y = ["Tom", 2.71, 36, 36] # is a list. MUTABLE
z = ("Tom", 2.71, 36, 36) # tuple is IMMUTABLE

print("x is a   SET : ", x)
print("y is a  LIST : ", y)
print("z is a TUPLE : ", z)
print("\n")
#=====================================================================
# CREATING list
arr = ['text', 78, 2.23, 'go', 70.2] # direct DECLARE elements
print(arr)

arr = list(range(5,30,5))             # using RANGE(start,stop,step)
print(arr)

arr = []                              # empty list + APPENDING
for i in range(1,10):
    arr.append((2*i)+3)
print(arr)

arr = [(2*x)+3 for x in range(1,10)]  # list COMPREHENSION
print(arr)
print("\n")
#=====================================================================
# INDEXING, SLICING and CONCATINATION
arr = ['text', 78, 2.23, 'go', 70.2]
brr = ["XYZ", 24902359]
print(arr)        # Prints complete list
print(arr[0])     # Prints 0th element of the list
print(arr[1:3])   # Prints sub-list from 1st till 3rd. 3rd excluded
print(arr[2:])    # Prints sub-list from 2nd element
print(arr[:2])    # Prints sub-list from start till 2nd element. 2nd excluded
print(brr * 2)    # Prints list two times
print(arr + brr)  # Prints concatenated list
print("\n")
#=====================================================================
# ALIASING
warm = ["red", "yellow", "orange"]
hot = warm  # hot and warm both point to same memory location
print(f"hot = {hot}")
print(f"warm = {warm}")
hot.append("pink")
print(f"hot = {hot}")  # 'hot' is an ALIAS for 'warm'
print(f"warm = {warm}")
print()
#=====================================================================
# CLONING
warm = ["red", "yellow", "orange"]
hot = warm[:]  # new memory assigned to 'hot'
print(f"hot = {hot}")
print(f"warm = {warm}")
hot.append("pink")
print(f"hot = {hot}")  # 'hot' is an CLONE for 'warm'
print(f"warm = {warm}")
print()
#=====================================================================

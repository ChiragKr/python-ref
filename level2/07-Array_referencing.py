__author__ = 'chira'

# set != array. Does not support indexing
# tuple != array. Does not support mutation
x = {1,9,2,3,1,7} # is a set. repetition NOT allowed
y = [1,9,2,3,1,7] # is an array/list. mutable
z = (1,9,2,3,1,7) # tuple. array but immutable

print("x is is a SET : ", x)
print("y is a list : ", y)
print("z is a tuple : ", z)
print("\n")

# ways to create and(or) populate arrays
arr = range(5,50,5)        # '50' not included
brr = []                   # an empty array. can append as we go along
for i in range(1,10):      # i iteratively takes on values form [1,2...8,9] array
    brr.append((2*i)+3)    # appending
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ] # direct declare elements
tinylist = [123, 'john']                    # direct declare elements

# reference to array elements
print list            # Prints complete list
print list[0]         # Prints 0th element of the list
print list[1:3]       # Prints elements starting from 1st till 3rd. 3rd excluded
print list[2:]        # Prints elements starting from 2nd element
print list[:2]        # Prints elements from starting till 2nd element. 2nd excluded
print tinylist * 2    # Prints list two times
print list + tinylist # Prints concatenated lists
print("\n")

# printing arrays
print(arr)
print("arr = {}".format(arr))

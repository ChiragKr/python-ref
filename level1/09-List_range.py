__author__ = 'chira'

# creating and traversing arrays
arr = [1,2,3,4,5]
print("arr = {}".format(arr)) # print(arr)
for arr_i in arr: # arr_i iteratively takes on values form arr in sequential order
    print(arr_i)

print('-------------')

arr = range(3,23,3)
print(arr)        # print("arr = {}".format(arr))
for arr_i in arr: # arr_i iteratively takes on values form arr in sequential order
    print(arr_i)

print('-------------')

arr = []              # creating and empty array to populate later
for i in range(1,10): # array will have 10-1 = 9 elements
    x = 2*i           # creating element
    arr.append(x)     # adding element to our array
print(arr)

print('-------------')
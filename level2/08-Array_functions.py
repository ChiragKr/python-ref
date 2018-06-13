__author__ = 'chira'

# initialising arrays
arr = range(5,50,5)   # '50' not included
brr = []                   # an empty array. can append as we go along
for i in range(1,10):      # 10 not included
    brr.append((3*i)+1)

# printing arrays
print("arr = {}".format(arr))
print("brr = {}".format(brr))

# common array manipulation functions
l = arr.__len__();                      # number of elements in arr
print("length of array = %d" %l)

indexOf = arr.index(30)                 # returns index of parameter
print("arr.index(30) = %d since 30 FIRST occurs at index = %d" %(indexOf,indexOf))

print("arr + brr = {}".format(arr+brr)) # concatenation of lists
print("brr + arr = {}".format(brr+arr))

crr = arr.__add__([109,298,327])        # same as concatenation
print("arr.__add__([109,298,327]) = {}".format(crr))
print("arr + [109,298,327]        = {}".format(arr + [109,298,327]))

arr.extend(brr)                         # equivalent to arr = arr + brr
print("arr.extend(brr) = {}".format(arr))

indexOf = arr.index(25)                 # returns index of parameter
print("arr.index(25) = %d since 25 FIRST occurs index = %d" %(indexOf,indexOf))

count = arr.count(25)                   # counts number or occurrences of 25 in arr
print("arr.count(25) = %d since 25 occurs %d times in arr" %(count,count))

print("arr             = {}".format(arr))

arr.append(32)                          # add 32 to arr. adds at the end of arr
print("arr.append(32)  = {}".format(arr))

val = arr.__contains__(25)              # checks if array contains parameter
print("arr.__contains__(25) = %d since array does contain 25" %(val))
val = arr.__contains__(23)              # checks if array contains parameter
print("arr.__contains__(23) = %d since array does NOT contain 23" %(val))

arr.remove(25)                          # removes 25 from arr. Removes only once even if occurs twice
print("arr.remove(25)  = {}".format(arr))

arr.insert(1,8)                         # add 8 to arr at index 1
print("arr.insert(1,8) = {}".format(arr))

t = arr.pop()                           # removes AND RETURNS last element of array
print("arr.pop() = %d since the last element of arr is %d " %(t,t))
print("arr after pop() = {}".format(arr))

t = arr.pop(5)                          # removes AND RETURNS the element at index 5
print("arr.pop(5) = %d since the 6th element of arr is %d " %(t,t))
print("arr after pop(5) = {}".format(arr))

arr.reverse()                           # reverses the array
print("arr.reverse()   = {}".format(arr))

arr.sort()                              # sorts array in increasing order
print("arr.sort()      = {}".format(arr))

print("arr = {}".format(arr))
print("brr = {}".format(brr))
isEqual = arr.__eq__(brr)               # checks if arrays are equal
print("arr.__eq__(brr) = %d since arr != brr" %isEqual)




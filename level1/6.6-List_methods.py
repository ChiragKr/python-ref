__author__ = 'Chirag'

arr = list(range(5,31,5))
brr = [(3*x)+1 for x in range(1,5)]
print("arr = {}".format(arr))
print("brr = {}".format(brr))
print("\n")
# list METHODS
l = arr.__len__();                      # number of elements in arr
print("arr.__len__() = %d" %l)
l = len(arr);                           # number of elements in arr
print("len(arr) = %d" %l)
print("\n")
indexOf = arr.index(30)                 # returns index of parameter
print("arr.index(30) = %d since 30 FIRST occurs at index = %d" %(indexOf,indexOf))
print("\n")
print("arr + brr = {}".format(arr+brr))# concatenation of lists
print("brr + arr = {}".format(brr+arr))
print("\n")
crr = arr.__add__([109,298,327])        # same as concatenation
print("arr.__add__([109,298,327]) = {}".format(crr))
print("arr + [109,298,327]        = {}".format(arr + [109,298,327]))
print("\n")
arr.extend(brr)                         # equivalent to arr = arr + brr
print("arr.extend(brr) = {}".format(arr))
print("\n")
indexOf = arr.index(25)                 # returns index of parameter
print("arr.index(25) = %d since 25 FIRST occurs index = %d" %(indexOf,indexOf))
print("\n")
count = arr.count(25)                   # counts number or occurrences of 25 in arr
print("arr.count(25) = %d since 25 occurs %d times in arr" %(count,count))
print("\n")
print("arr             = {}".format(arr))
print("\n")
arr.append(32)                          # add 32 to arr. adds at the end of arr
print("arr.append(32)  = {}".format(arr))
print("\n")
val = arr.__contains__(25)              # checks if array contains parameter
print("arr.__contains__(25) = %d since array does contain 25" %(val))
val = arr.__contains__(23)              # checks if array contains parameter
print("arr.__contains__(23) = %d since array does NOT contain 23" %(val))
print("\n")
arr.remove(25)                          # removes 25 from arr. Removes only once even if occurs twice
print("arr.remove(25)  = {}".format(arr))
print("\n")
arr.insert(1,8)                         # add 8 to arr at index 1
print("arr.insert(1,8) = {}".format(arr))
print("\n")
t = arr.pop()                           # removes AND RETURNS last element of array
print("arr.pop() = %d since the last element of arr is %d " %(t,t))
print("arr after pop() = {}".format(arr))
print("\n")
t = arr.pop(5)                          # removes AND RETURNS the element at index 5
print("arr.pop(5) = %d since the 6th element of arr is %d " %(t,t))
print("arr after pop(5) = {}".format(arr))
print("\n")
arr.reverse()                           # reverses the array
print("arr.reverse()   = {}".format(arr))
print("\n")
arr.sort()                              # sorts array in increasing order
print("arr.sort()      = {}".format(arr))
print("\n")
print("arr = {}".format(arr))
print("brr = {}".format(brr))
isEqual = arr.__eq__(brr)               # checks if arrays are equal
print("arr.__eq__(brr) = %d since arr != brr" %isEqual)




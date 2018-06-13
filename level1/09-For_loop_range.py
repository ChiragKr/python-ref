__author__ = 'chira'

#range(a,stop,d) = [a, a+d, a+2d, a+3d,..., a+nd] such that a+nd < stop (strictly less than)

for x in range(10):       # x iteratively takes on values form [0,1,...,8,9] array in sequential order
    print(x)

print('---')

for x in range(5, 12):    # x iteratively takes on values form [5,6,...,10,11] array in sequential order
    print(x)

print('---')

for x in range(5, 40, 5): # x iteratively takes on values form [5,10,15,...,30,35] array in sequential order
    print(x)

# for-loop   : when number of iterations known
# while-loop : when iteration depends on condition

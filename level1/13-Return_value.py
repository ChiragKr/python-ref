__author__ = 'chira'

# "return" used for mathematical function composition

def f(x):    # x is an INPUT
    y = 2*x + 3
    return y # y is an OUTPUT

def g(x):    # x is an INPUT
    y = pow(x,2)
    return y # y is an OUTPUT

def h(x,y):  # x and y are INPUTS
    z = pow(x,2) + 3*y;
    return z # z is an OUTPUT

output = 0        # initializing a variable to store return values
output = f(1)     # return form "f" stored in output
print("f(%d) = %d" %(1,output))

output = g(5)
print("g(%d) = %d" %(5,output))

output = f(25)
print("f(%d) = %d" %(25,output))

output = f(g(5))  # return form "g" is input to "f"
print("f(g(%d)) = %d" %(5,output))

output = h(5,25)
print("h(%d,%d) = %d" %(5,25,output))

output = h(f(1),g(5)) # returns form "f" and "g" are inputs to "h"
print("h(f(%d),g(%d)) = %d" %(1,5,output))

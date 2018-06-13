__author__ = 'chira'

# "def" as defining mathematical functions
# 18-Unpacking_args gives an alternate way to pass arguments

def f(x):   # function name is "f". NOTE it has ONE argument
    y = 2*x + 3
    print("f(%d) = %d" %(x,y))

def g(x):   # function name is "g". NOTE it has ONE argument
    y = pow(x,2)
    print("g(%d) = %d" %(x,y))

def h(x,y): # function name is "h". NOTE it has TWO arguments
    z = pow(x,2) + 3*y;
    print("h(%d,%d) = %d" %(x,y,z))


f(1)# call (by value)
f(3)
g(5)
h(2,3)

# for doing a function composition we need the notion of "return" values
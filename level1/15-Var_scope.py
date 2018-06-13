__author__ = 'chira'

'''basic understanding of "scope of a variable"'''

'''
comment out section(a) and run section(b)
'''

# section(a) starts
x = 393      #GLOBAL VARIABLE. Every function can use

def func1():
    print(x)

def func2():
    print(x)

func1()
func2()
# section(a) ends

'''
# section(b) starts

def func1():
    x = 393 #LOCAL VARIABLE. Only use in function where it is declared
    print(x)

def func2():
    print(x)

func1()
func2()
# section(b) ends
'''
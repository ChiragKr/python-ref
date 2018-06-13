__author__ = 'Chirag'

#==========================================
s = "Hello World" # creating string
print(s) # printing (entire) string

x = len(s) # number of characters in string
print(x) #--> 11

x = s[6]   # string INDEXING
print(x) #--> W

x = s[4:9] # string SLICING
print(x) #--> o Wor
x = s[4:]
print(x) #--> lo World
x = s[:4]
print(x) #--> Hell

print(s * 2) #--> Hello WorldHello World

s = s + "TEST" # string CONCATINATION
print(s+ "TEST") #--> Hello WorldTEST
#==========================================
#SOME USEFUL BUILT-IN STRING METHODS
s = "Hello World! What's UP?"

x = s.upper() #CONVERTS to uppercase
print(x) #--> HELLO WORLD! WHAT'S UP

x = s.lower() #CONVERTS to uppercase
print(x) #--> hello world! what's up?

x = s.split(" ") #LIST of words seperated by " "
print(x) #--> ['Hello', 'World!', "What's", 'UP?']

s = "-".join(x) #STRING concat list items with '-'
print(s) #--> Hello-World!-What's-UP?
#==========================================



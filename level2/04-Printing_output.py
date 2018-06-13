__author__ = 'chira'

name = "Chirag"
DOB = "21/12/1996"
age = 21
ID = "2016B4A70752G"
year = 2
CGPA = 8.98

print ("Hey there! My name is %s." %name)
print ("I was born on %s. I am %d years old. " %(DOB, age))
print ("I am in my %d year of college with a CGPA of %.3f" %(year, CGPA)) # formatting float

print ("\n") # special character for "enter" key. changes lines

# using type casting and string concatenation
print ("Hey there! My name is " + name)
print ("I was born on " + DOB + ". I am " + str(age) + " years old. ")
print ("I am in my " + str(year) + " year of college with a CGPA of " + str(CGPA))
print("\n")

# printing arrays
arr = range(5,50,5)
print(arr)
print("arr = {}".format(arr))
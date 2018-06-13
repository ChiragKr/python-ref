__author__ = 'chira'

name, age = "Chirag", 21
DOB = "21/12/1996"
ID = "2016B4A70752G"
year, CGPA = 2, 8.98

#================================================================================================
#						    METHOD 1 (using type conversion and concatination)
#================================================================================================
print ("Hey there! My name is " + name)
print ("I was born on " + DOB + ". I am " + str(age) + " years old. ")
print ("I am in my " + str(year) + " year of college with a CGPA of " + str(CGPA))
print("\n")
#================================================================================================
#						    METHOD 2 (using '%' sting operator)
#================================================================================================
print ("Hey there! My name is %s." %name)
print ("I was born on %s. I am %d years old. " %(DOB, age))
print ("I am in my %02d year of college with a CGPA of %1.3f" %(year, CGPA)) # formatting float
print("\n")
#================================================================================================
#						    METHOD 3 (using .format() function)
#================================================================================================
print ("Hey there! My name is {}.".format(name))
print ("I was born on {x}. I am {y} years old. ".format(y = age, x = DOB))
print ("I am in my {0:02d} year of college with a CGPA of {1:1.3f}".format(year,CGPA))
print("\n")
#================================================================================================
#						    METHOD 4 (using f-strings)
#================================================================================================
print (f"Hey there! My name is {name}.")
print (f"I was born on {DOB}. I am {age} years old. ")
print (f"I am in my {year} year of college with a CGPA of {CGPA}")
print("\n")
#================================================================================================

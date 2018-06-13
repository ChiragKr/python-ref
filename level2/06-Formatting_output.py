__author__ = 'chira'

year = 2
CGPA = 8.98

# string modulo operator
print ("I am in my %d year of college with a CGPA of %f" %(year, CGPA)) # formatting using format specifiers
print ("I am in my %2d year of college with a CGPA of %.2f" %(year, CGPA)) # formatting using format specifiers
print ("I am in my %3d year of college with a CGPA of %.3f" %(year, CGPA)) # formatting using format specifiers
print ("I am in my %3d year of college with a CGPA of %8.3f" %(year, CGPA)) # formatting using format specifiers
print("\n")

# string concatenation
print ("I am in my " + str(year) + " year of college with a CGPA of " + str(CGPA))
print("\n")

# the format() function
print ("I am in my {0:5d} year of college with a CGPA of {1:.3f}".format(year, CGPA)) # format()
print ("I am in my {a:5d} year of college with a CGPA of {b:.3f}".format(a = year, b = CGPA))
print ("I am in my {yr} year of college with a CGPA of {cg}".format(yr = year, cg = CGPA))
arr = range(5,50,5)
print("arr = {}".format(arr))
print("\n")

#other useful formatting functions
s = "Python"
print(s.center(10))
print(s.center(10,'*'))
print(s.ljust(10))
print(s.ljust(10,'#'))
print(s.rjust(10))
print(s.rjust(10,'#'))

foods = ["bacon","tuna","ham","beef","milk"]
for f in foods:
    print("%s %2d" %(f.ljust(6),len(f))) # try s.rjust()
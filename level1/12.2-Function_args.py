__author__ = 'Chirag'

'''converts celsius to fahrenheit
NOTE : ARGUMENTS required for function
i.e the Temperature in Celsius.'''


# Function has NO arguments/INPUTS
def func():
    print("You called func()! ")
    print("The block of code inside func() is being executed")
    x = 2.345
    print(f"value of x (a variable inside func()) is = {x}")
    print(f"sqrt(x) = {x**0.5}")


# Function has ONE as argument/INPUT, i.e "temp_in_celsius"
def convert_to_fahrenheit(temp_in_celsius):
    temp_in_fahrenheit = ((9/5)*temp_in_celsius + 32)
    print("{0:3d} \u00b0C = {1:7.3f} \u00b0F".format(temp_in_celsius, temp_in_fahrenheit))


func()
print()
# passing argument. A "call by value".
convert_to_fahrenheit(100)

'''
in above case call to function convert_to_fahrenheit
goes with a parameter whose VALUE GETS COPIED
(call by value) therefore temp_in_celsius = 3.85.
'''

# code re-usability
convert_to_fahrenheit(37)
convert_to_fahrenheit(0)

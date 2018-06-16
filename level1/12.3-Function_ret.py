__author__ = 'Chirag'

'''Certain times we want the function to make certain
calculations but not print it just yet, rather to STORE
it and use it later. This is where we use 'return' keyword'''


def convert_to_fahrenheit(temp_in_celsius): # argument/INPUT to function
    temp_in_fahrenheit = ((9/5)*temp_in_celsius + 32)
    return temp_in_fahrenheit               # return/OUTPUT form function


def print_result(temp_in_celsius, temp_in_fahrenheit):
    print("{0:3d} \u00b0C = {1:7.3f} \u00b0F".format(temp_in_celsius, temp_in_fahrenheit))


for temp_in_celsius in range(101):
    temp_in_fahrenheit = convert_to_fahrenheit(temp_in_celsius)
    print_result(temp_in_celsius, temp_in_fahrenheit)

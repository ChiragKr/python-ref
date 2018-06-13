__author__ = 'chira'

'''
setting default values to arguments of function
Eg. getting gender on a social media profile
'''

# def <function name>(argument1, argument2,....):

# if NO INPUT GIVEN then the input value BY DEFAULT is "Unknown"
def getGender(sex = 'Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)

getGender('m')
getGender('f')
getGender() # input NOT given, therefore DEFAULT input considered

__author__ = 'chira'

'''setting default values to arguments of function
Eg. getting gender on a social media profile'''


# if NO INPUT GIVEN then the input value BY DEFAULT is "Unknown"
def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)


get_gender('m')
get_gender('f')
get_gender()  # input NOT given, therefore DEFAULT input considered

__author__ = 'chira'

'''
Just like an ordinary dictionary, with words and their
definitions, Python also has a dictionary implementation,
which takes a 'KEY'(the word) and 'VALUE'(the definition)
KEY <------> VALUE
'''

# <dictionary name> = {key1: val1, key2: val2,...}

classmates = {'Tony': 'JERK',
              'Emma': 'SWEET',
              'Lucy': 'GENIUS'}

print(classmates)         # prints entire dictionary

print(classmates['Emma']) # prints VALUE of a given KEY

for k, v in classmates.items(): # Special Syntax for dictionary
    print('%s : %s' %(k,v))
__author__ = 'chira'

'''
SETS : a collection of UNIQUE items
List - CAN have DUPLICATE items,
Set  - CANNOT have DUPLICATE items.
'''

# NOTE : 'milk' is entered twice
groceries = {'cereal', 'milk', 'eggs', 'lotion', 'milk'}
Groceries = ['cereal', 'milk', 'eggs', 'lotion', 'milk']

print("set  : {}".format(groceries))
print("list : {}".format(Groceries))


'''
# checking if item is in set or not
if 'cereal' in groceries: # checks each element of set "groceries" for EQUALITY with string "cereal"
    print('You already have cereal!')
else:
    print('Oh yeah! You need cereal!')

if 'cheese' in groceries: # checks each element of set "groceries" for EQUALITY with string "cheese"
    print('You already have cheese!')
else:
    print('Oh yeah! You need cheese!')
'''

def checkIfPresent(s):
    if s in groceries: # checks each element of set "groceries" for EQUALITY with string s
        print('You already have %s!'%s)
    else:
        print('Oh yeah! You need %s!'%s)

# code reusability
checkIfPresent('cereal')
checkIfPresent('cheese')
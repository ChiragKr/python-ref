__author__ = 'Chirag'

'''
lists and tuple related to mathematical SEQUENCES
     dictionary related to mathematical MAPPING
'''
#==============================================
# CREATING dictionary
# <name> = {key1: val1, key2: val2,...}
# values can be anything (even other dictionary)
my_dict = {
    'key1': 365,
    'key2': 'SWEET',
    'key3': [2,3,4,5],
    'key4': {
        'k1' : 10,
        'k2' : 100,
    },
    'key5': False
}
#==============================================
# ACCESSING dictionary objects
x = my_dict['key2']
print(x) #--> SWEET

x = my_dict['key3'][2]
print(x) #--> 4

x = my_dict['key4']['k2']
print(x) #--> 100

# my_dict.items() = list of tuples of all items
# therefore, using TUPLE unpacking concept
for k, v in my_dict.items():
    print('%s : %s' %(k,v))
print()
#==============================================
# REASSIGNMENT
my_dict = {'k1':1,'k2':2,'k3':3}
print(my_dict)
my_dict['k3'] = "choco"
print(my_dict)
print()
#==============================================
# dictionary METHODS
my_dict = {'k1':1,'k2':2,'k3':3}
print(f"my_dict = {my_dict}\n")
x = my_dict.items()
print(f"my_dict.items()  = {x} | type = {type(x)}\n")
x = my_dict.keys()
print(f"my_dict.keys()   = {x} | type = {type(x)}\n")
x = my_dict.values()
print(f"my_dict.values() = {x} | type = {type(x)}\n")
#==============================================

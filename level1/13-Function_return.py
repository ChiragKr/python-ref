__author__ = 'chira'

'''
Certain times we want the function to make certain
calculations but not print it just yet, rather to STORE
it and use it later. This is where we use 'return' keyword
'''

def allowed_dating_age(my_age): # ONE as argument/INPUT
    girls_age = (my_age/2) + 7
    return girls_age            # return/OUTPUT form function

chirags_limit = allowed_dating_age(22)
print('Chirag can date girls %d or older' % chirags_limit)

creepy_mike_limit = allowed_dating_age(39)
print('Creepy Mike can date girls %d or older' % creepy_mike_limit)

print("dude's age - limit (>)")
for n in range(20,40):
    print("    %d     -     %d  " %(n,allowed_dating_age(n)))


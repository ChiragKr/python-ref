__author__ = 'chira'

'''
def <function name>(keyword_1 = default_val1, keyword_2 = default_val2...):
    ....
    ....
during function call you can specify SOME or ALL arguments
function name(keyword_i = value_i, keyword_j = value_j...)'''


# parameter passing flexibilities
def dumb_sentence(name = 'Chirag', action = 'ate', item = 'kebabs'):
    print("%s %s %s." % (name, action, item))


# =======================================================
# input NOT GIVEN. (DEFAULT ARGUMENTS)
dumb_sentence()
print()
# =======================================================
# inputs GIVEN (POSITIONAL ARGUMENTS)
dumb_sentence('Sally', 'walks', 'slowly')
dumb_sentence('Sally', 'slowly', 'walks')
print()
# =======================================================
# inputs GIVEN (KEYWORD ARGUMENTS)
dumb_sentence(item='pizza')  # limited args. remaining take DEFAULT values
dumb_sentence(item='juice', action='drank')  # limited args. Any order. remaining take DEFAULT values
print()
# =======================================================

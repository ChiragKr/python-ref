__author__ = 'chira'

'''function signature flexibilities'''

def dumb_sentence(name = 'Chirag', action = 'ate', item = 'kebabs'):
    print("%s %s %s." % (name, action, item))

dumb_sentence()                            # NO INPUT => default values considered
dumb_sentence('Sally', 'walks', 'slowly')  # inputs GIVEN
dumb_sentence(item='pizza')                # limited args. REST IS DEFAULT
dumb_sentence(item='juice', action='drank')# limited args. Any order. REST IS DEFAULT

'''
def <function name>(keyword_1 = default_val1, keyword_2 = default_val2...)
    ....
    ....
during function call you can specify SOME or ALL arguments
function name(keyword_i = value_i, keyword_j = value_j...)
'''
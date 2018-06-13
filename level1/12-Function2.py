__author__ = 'chira'

'''
converts bitcoin to INR
NOTE : ARGUMENTS required for function
i.e the number of bit coins available
'''

def bitcoin_to_inr(btc): # function has ONE argument
    amount = btc * 527 * 68
    print("amount = %d" % amount)

def beef():              # function has NO arguments
    print('Dayum, functions are cool!')
    print("but this function has no arguments! :(")

beef()
bitcoin_to_inr(3.85) # call by value

'''
in above case call to function bitcoin_to_inr
goes with a parameter whose VALUE GETS COPIED
(call by value) therefore btc = 3.85.
'''

# code re-usability
bitcoin_to_inr(2.625)
bitcoin_to_inr(1.255)

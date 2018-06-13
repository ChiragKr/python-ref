__author__ = 'chira'

# WHILE-loop : to proceed with iteration based on condition
# FOR-loop   : to proceed with iteration based on value

x = 5
while x < 10:        # checks condition is x < 10. If yes, then proceed with loop
    print(x)
    x += 1

print("------------");

x = 5
while x in range(10):# checks if x is EQUAL TO ANY ELEMENT in [0,1...9]
    print(x)
    x += 1

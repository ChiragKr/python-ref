_author__ = 'chira'

magicNumber = 45

# this program finds a magic number

for n in range(100): # n iteratively takes values [0,1,2...98,99] sequentially
    if n is magicNumber: # if n == magicNumber
        print("%d is the magic number!" % n)
        break
    else:
        print(n)

# break    : terminates loop completely. Moves outside the loop
# continue : terminates current iteration. Moves to next iteration
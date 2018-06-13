__author__ = 'chira'

age = 19.5

if age < 21:                  # INEQUALITY check
    print("NO Beer for you!")
else:
    print("you can have beer")

if age in range(1,21):        # checks EACH element of list = [1,2,3...,19,20] for EQUALITY
    print("NO Beer for you!")
else:
    print("you can have beer")

key = 10                      # change value to 6 and analyse output
lock_list = [5, 12, 4, 3, 6, 1, 2]

for n in lock_list:           # n iteratively takes on values for lock_list array
    if n is key:              # equivalently 'if n == key'
        break
    else:
        print(n)

if key in lock_list:          # checks EACH element of lock_list for EQUALITY
    print("list is un-lockable!")
else:
    print("list is locked forever!")
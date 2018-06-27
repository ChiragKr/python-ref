_author__ = 'chira'

numbersTaken = [2, 5, 8, 12, 13]

# break    : terminates loop completely. Moves outside the loop
# continue : terminates current iteration. Moves to next iteration

print('Here are the numbers available')
for n in range(1,15):
    if n in numbersTaken:
        continue # skip current iteration and start next iteration
    print(n)
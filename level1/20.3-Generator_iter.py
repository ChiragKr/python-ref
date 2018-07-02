__author__ = 'Chirag'

'''iter(<iterable>) = iterator converts 
iterable object into in 'iterator' so that 
we use can use the next(<iterator>)'''

string = "Hello"

for letter in string:
	print(letter)

string_iter = iter(string)
print(next(string_iter))

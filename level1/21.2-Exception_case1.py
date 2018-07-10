__author__ = 'Chirag'

while True:
	try:
		n = input("Please enter an integer: ")
		n = int(n)
		break
	except ValueError:
		print("Input not an integer. Try Again!")
print("Correct!")

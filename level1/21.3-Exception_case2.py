__author__ = 'Chirag'

text = ""

file_name = input("Please provide a file name : ")  # "fileWriteDemo1.txt"

try:
	my_file = open(file_name, 'r')

except IOError:
	print("cannot open ", file_name)

else:
	lines = my_file.readlines() # list of individual lines
	for line_num, line in enumerate(lines):
		print(f"{line_num} : {line}")

finally:
	my_file.close()

__author__ = 'Chirag'

# text file is expected to be in same folder as the script. However we can explicitly give
# the full path also eg. "/home/chirag/PycharmProjects/python-ref/fileWriteDemo1.txt"

print("===========================================")
myfile = open('fileWriteDemo1.txt', 'r')
text = myfile.read()
print(text)

text = myfile.read()
print(text) # --> will print '' as file has already been read and cursor is at the end of the file
cursor_position = myfile.seek(0) # --> reset cursor position to '0' index of the file string

text = myfile.read()
print(text) # --> now the file is read properly (however cursor_position is at the end of the file)
myfile.close()

print("===========================================")
# ALTERNATE SYNTAX
with open("fileWriteDemo1.txt", 'r') as myfile:
	text = myfile.read()
	print(text)

print("===========================================")
with open("fileWriteDemo1.txt", 'r') as myfile:
	lines = myfile.readlines() # list of individual lines
	for line_num, line in enumerate(lines):
		print(f"{line_num} : {line}")

print("===========================================")

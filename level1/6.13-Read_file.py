__author__ = 'Chirag'

# text file is expected to be in same folder as the script. However we can explicitly give
# the full path also eg. "/home/chirag/PycharmProjects/python-ref/fileWriteDemo1.txt"

print("===========================================")
myfile = open('fileWriteDemo1.txt', 'r')
text = myfile.read()
print(text)
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

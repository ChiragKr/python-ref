__author__ = 'Chirag'

# by default text file edited/created in same folder as the script. However we can explicitly
# give the full path also eg. "/home/chirag/PycharmProjects/python-ref/fileWriteDemo1.txt"

# in 'w' mode file is over written
myfile = open("fileWriteDemo1.txt", 'w')
print(f"type(myfile) = {type(myfile)}")
myfile.write("writing some stuff to my new file, \n")
myfile.write("fileWriteDemo1.txt via script 6.12-Write_file.py")
myfile.close()

# ALTERNATE SYNTAX
with open("fileWriteDemo2.txt", 'w') as myfile:
	myfile.write("ALTERNATE WAY OF WRITING THING TO FILE\n")
	myfile.write("WITHOUT WORRYING ABOUT CLOSING THE FILE USING .close()")

# in 'a' mode file is appened
with open("fileWriteDemo1.txt", 'a') as myfile:
	myfile.write("\nTHIS LINE WAS APPENDED TO fileWriteDemo1.txt \n")
	myfile.write("by using the append mode of file writing")

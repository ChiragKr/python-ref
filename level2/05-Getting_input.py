__author__ = 'chira'

# input() automatically detects the data type
# raw_input() takes all inputs as a string

name = raw_input("Enter name : ")
id_no = raw_input("BITS ID : ")

age_raw = raw_input("Age : ")
age_int = input("Age : ")

print(age_raw, "age input by raw_input() is of data type", type(age_raw)) # raw_input() assigns data type in STRING
print(age_int, "age input by input() is of data type", type(age_int)) # input() data type in INT

CGPA_raw = raw_input("CGPA : ")
CGPA_flt = input("CGPA : ")

print(CGPA_raw, "CGPA input by raw_input() is of data type", type(CGPA_raw)) # raw_input() assigns datatype in STRING
print(CGPA_flt, "CGPA input by input() is of data type", type(CGPA_flt)) # input() data type in FLOAT

age_str = str(age_int) # type casting
CGPA_str = str(CGPA_flt) # type casting

print(age_str, "age_str is of data type (type casting)", type(age_str))
print(CGPA_str, "CGPA_str is of data type (type casting)", type(CGPA_str))





__author__ = 'chira'

age = 21
CGPA = 8.98

# type() used to detect type of data tye
print(age, "age is of data type", type(age))
print(CGPA, "CGPA is of data type", type(CGPA))

# str() - coverts parameter to string data type
age_str = str(age)
CGPA_str = str(CGPA)

print(age_str, "age_str is of data type (type casting)", type(age_str))
print(CGPA_str, "CGPA_str is of data type (type casting)", type(CGPA_str))

# int() - coverts parameter to int data type
# float() - coverts parameter to float data type

age_flt = float(age) # integer to float type casting
print(age_flt, "age_flt is of data type (type casting)", type(age_flt))

CGPA_int = int(CGPA) # float to integer type casting
print(CGPA_int, "CGPA_int is of data type (type casting)", type(CGPA_int))
__author__ = 'Chirag'

my_int = 153
my_flt = 2.7
#============================================================
# type() used to detect type of data tye
print(f"my_int = {my_int} and type(my_int) = {type(my_int)}")
print(f"my_flt = {my_flt} and type(my_flt) = {type(my_flt)}")
print()
#============================================================
# str() - coverts parameter to string data type
my_int_str = str(my_int)
my_flt_str = str(my_flt)
print(f"my_int_str = str(my_int) = {my_int_str} is of data type {type(my_int_str)}")
print(f"my_flt_str = str(my_flt) = {my_flt_str} is of data type {type(my_flt_str)}")
print()
#============================================================
# int() - coverts parameter to int data type
my_flt_int = int(my_flt)
print(f"my_flt_int = int(my_flt) = {my_flt_int} is of data type {type(my_flt_int)}")
print()
#============================================================
# float() - coverts parameter to float data type
my_int_flt = float(my_int)
print(f"my_int_flt = float(my_int) = {my_int_flt} is of data type {type(my_int_flt)}")
print()
#============================================================

# list() - converts parameter to a list
s = {1,2,3,4}
l = list(s)
print(f"s = {s} is of type = {type(s)}")
print(f"list(s) = {l} is of type = {type(l)}")
t = (1,2,3,4)
l = list(t)
print(f"t = {t} is of type = {type(t)}")
print(f"list(t) = {l} is of type = {type(list(l))}")
print()
#============================================================
# set() - converts parameter to a set
l = [1,2,3,4]
s = set(l)
print(f"l = {l} is of type = {type(l)}")
print(f"set(l) = {s} is of type = {type(s)}")
t = (1,2,3,4)
s = set(t)
print(f"t = {t} is of type = {type(t)}")
print(f"set(t) = {s} is of type = {type(s)}")
print()
#============================================================
# tuple - converts parameter to a tuple
l = [1,2,3,4]
t = tuple(l)
print(f"l = {l} is of type = {type(l)}")
print(f"tuple(l) = {t} is of type = {type(t)}")
s = {1,2,3,4}
t = tuple(s)
print(f"s = {s} is of type = {type(s)}")
print(f"tuple(s) = {t} is of type = {type(t)}")
print()
#============================================================

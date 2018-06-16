__author__ = 'Chirag'


#===========================================================================================
def is_prime(num):
	num_of_factors = 0
	factor = 1
	while factor <= num:
		if num % factor == 0:
			num_of_factors += 1
		factor += 1

	if num_of_factors == 2:
		return True
	else:
		return False
#===========================================================================================
# map(function, iterable) quickly call the same function to every item in an iterable
nums = list(range(1,11))
is_prime_map = list(map(is_prime, nums))
print(f"nums = {nums}")
print("is_prime_map = list(map(is_prime, nums))")
print(f"is_prime_map = {is_prime_map}")
print()
#===========================================================================================
# filter(function, iterable)
is_prime_filter = list(filter(is_prime, nums))
print("is_prime_filter = list(filter(is_prime, nums))")
print(f"is_prime_filter = {is_prime_filter}")
print()
#===========================================================================================
# lambda expressions helps create "anonymous" functions (ad-hoc functions without using def)
def square(num):
	return num**2
# the corresponding lambda expression on 'square' function above
# lambda num: num ** 2
nums = list(range(1,11))
print(f"nums = {nums}")
l = list(map(lambda num: num ** 2, nums))
print("l = list(map(lambda num: num ** 2, my_nums))")
print(f"l = {l}")
#===========================================================================================

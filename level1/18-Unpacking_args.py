__author__ = 'chira'

'''alternate way to send arguments using TUPLE UNPACKING'''


def health_calculator(age, apples_ate, cigs_smoked):
    rating = (100-age)+(apples_ate*0.25)-(cigs_smoked*2)
    print(rating)


my_data = (20, 7, 0)
print(type(my_data))

health_calculator(my_data[0], my_data[1], my_data[2])
health_calculator(20, 7, 0)

# Alternatively we can unpack the
# tuple and send as arguments directly as
health_calculator(*my_data)


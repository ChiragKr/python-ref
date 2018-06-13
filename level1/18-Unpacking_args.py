__author__ = 'chira'

'''alternate way to send arguments using a lists'''

def health_calculator(age, apples_ate, cigs_smoked):
    rating = (100-age)+(apples_ate*0.25)-(cigs_smoked*2)
    print(rating)

chirags_data = [20, 7, 0]

health_calculator(chirags_data[0], chirags_data[1], chirags_data[2])
health_calculator(20,7,0)

# alternatively we can unpack the list and send as arguments directly
health_calculator(*chirags_data)


__author__ = 'chira'

food_list = ["bacon","tuna","ham","beef","milk","eggs","cookies","chicken","fish"]

for f in food_list:      # f iteratively takes on values form food_list array in sequential order
    print("%d----%s %2d" %(food_list.index(f), f.ljust(7),len(f)))

print('---------------')

for f in food_list[:5]:  # f iteratively takes on values form food_list array beginning to 5th. 5th excluded
    print("%d----%s"%(food_list.index(f),f))

print('---------------')

for f in food_list[2:6]: # f iteratively takes on values form food_list array from 2nd to 6th. 6th excluded
    print("%d----%s"%(food_list.index(f),f))

print('---------------')

for f in food_list[3:]:  # f iteratively takes on values form food_list array from 3rd till end
    print("%d----%s"%(food_list.index(f),f))

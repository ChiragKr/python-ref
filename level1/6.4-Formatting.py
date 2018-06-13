__author__ = 'Chirag'

print('This is my ten-character, two-decimal number:%10.2f' %13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))

print("==============================")
# field lengths
print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

print("==============================")
# alignment + padding
print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

print("==============================")
# alignment + padding + padding character
print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))
print("==============================")

#other useful formatting functions
s = "Python"
print(s.center(10))
print(s.center(10,'*'))
print(s.ljust(10))
print(s.ljust(10,'#'))
print(s.rjust(10))
print(s.rjust(10,'#'))

foods = ["bacon","tuna","ham","beef","milk"]
for f in foods:
    print("%s %2d" %(f.ljust(6),len(f))) # try s.rjust()

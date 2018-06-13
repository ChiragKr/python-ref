__author__ = 'chira'

class ComplexNumber:

    def __init__(self, realPart, imgPart):
        self.r = realPart
        self.i = imgPart

    def display(self):
        s = str(self.r) + " + "+str(self.i)+"i"
        return s

    def addition(self, a, b):
        self.r = a.r + b.r
        self.i = a.i + b.i

    def multiply(self, a, b):
        self.r = (a.r*b.r) - (a.i*b.i)
        self.i = (a.r*b.i) + (a.i*b.r)

    def negative(self, a):
        self.r = -1*a.r
        self.i = -1*a.i

    def reciprocal(self, a):
        d = float(pow(a.r,2) + pow(a.i,2))
        self.r = float((a.r))/d
        self.i = float((-1*a.i))/d

'''
z0 = ComplexNumber(0, 0)
z1 = ComplexNumber(2, 3)
z2 = ComplexNumber(3, 1)

print("     z1 = %s" %z1.display())
print("     z2 = %s" %z2.display())

z0.addition(z1,z2)
print("z1 + z2 = %s" %z0.display())

z0.multiply(z1,z2)
print("z1 * z2 = %s" %z0.display())

print("     z2 = %s" %z2.display())
z0.negative(z2)
print("    -z2 = %s" %z0.display())

z0.reciprocal(z2)
print("   1/z2 = %s" %z0.display())
'''
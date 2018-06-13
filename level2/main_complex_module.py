__author__ = 'chira'

import complex_module

z0 = complex_module.ComplexNumber(0, 0)
z1 = complex_module.ComplexNumber(2, 3)
z2 = complex_module.ComplexNumber(3, 1)

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
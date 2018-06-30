__author__ = 'Chirag'
# Operator overloading
import math

class Complex(object):

	def __init__(self, real, imaginary):
		self.real = real
		self.imaginary = imaginary

	def __add__(self, no):
		res_real = self.real + no.real
		res_img = self.imaginary + no.imaginary
		return Complex(res_real, res_img)

	def __sub__(self, no):
		res_real = self.real - no.real
		res_img = self.imaginary - no.imaginary
		return Complex(res_real, res_img)

	def __mul__(self, no):
		res_real = (self.real*no.real) - (self.imaginary*no.imaginary)
		res_img = (self.real*no.imaginary) + (self.imaginary*no.real)
		return Complex(res_real, res_img)

	def mod(self):
		res = Complex(0,0)
		res.real = (self.real**2 + self.imaginary**2)**0.5
		return res

	def __truediv__(self, no):
		res = Complex(0,0)
		res = self * Complex(no.real, -1*no.imaginary)
		deno = (no.real**2 + no.imaginary**2)
		res.real /= deno
		res.imaginary /= deno
		return res

	def __str__(self):
		if self.imaginary == 0:
			result = "%.2f+0.00i" % (self.real)
		elif self.real == 0:
			if self.imaginary >= 0:
				result = "0.00+%.2fi" % (self.imaginary)
			else:
				result = "0.00-%.2fi" % (abs(self.imaginary))
		elif self.imaginary > 0:
			result = "%.2f+%.2fi" % (self.real, self.imaginary)
		else:
			result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
		return result

if __name__ == '__main__':
	c = map(float, input().split())
	d = map(float, input().split())
	x = Complex(*c)
	y = Complex(*d)
	print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')

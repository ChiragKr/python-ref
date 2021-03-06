__author__ = 'Chirag'


class XY:
    x, y = 3, 2             # class variable SAME for ALL instances.

    def __init__(self, A):
        self.a = A          # instance variable DIFFERENT for each instance.

    def f(self, p=0, q=0):  # class function can be used by instances
        return (p+q)*self.a

    def status(self, name):
        print(name)
        print("\t class variables (x,y) = (%d,%d)"%(self.x, self.y))
        print("\t instance variable a = %d" % self.a)


Obj1 = XY(72)  # instantiation
Obj2 = XY(31)  # instantiation

# attribute referencing <object name>.<function name>
Obj1.status("Obj1")
Obj2.status("Obj2")

# attribute referencing <object name>.<function name>
print("Obj1.f(2,3) = %d" % Obj1.f(2,3))
print("Obj2.f(2,3) = %d" % Obj2.f(2,3))

print("\nchanging Obj2's INSTANCE variable value\n")
# attribute referencing <object name>.<variable name>
Obj2.a = 35  # Bad practice! should use 'setter' method instead

Obj1.status("Obj1")
Obj2.status("Obj2")

print("Obj1.f(2,3) = %d" % Obj1.f(2,3))
print("Obj2.f(2,3) = %d" % Obj2.f(2,3))

print("\nchanging CLASS variable values\n")
# class variable referencing <class name>.<variable name>
XY.x = 5
XY.y = 7

Obj1.status("Obj1")
Obj2.status("Obj2")

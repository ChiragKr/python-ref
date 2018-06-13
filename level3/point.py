__author__ = 'Chirag'

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def coordinates(tag, A):
        print('point',tag,' = (',A.x,',', A.y,')')

    def dist(A, B):
        x2 = (A.x - B.x) ** 2
        y2 = (A.y - B.y) ** 2
        d = (x2 + y2) ** 0.5
        return d;

    def main():
        o = Point()
        p = Point(4,5)
        q = Point(8,10)
        Point.coordinates('o', o)
        Point.coordinates('p', p)
        Point.coordinates('q', q)
        res = Point.dist(p,q)
        print(res)

Point.main()

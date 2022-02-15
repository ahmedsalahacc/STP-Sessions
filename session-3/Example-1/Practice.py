# @TODO complete the point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceFrom(self, p2):
        return ((self.x - p2.x)**2 + (self.y - p2.y)**2)**0.5

# @todo complete the Line class


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def getLength(self):
        return self.p1.distanceFrom(self.p2)

# @TODO complete The triangle class


class Triangle:
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def getPerimeter(self):
        return self.l1.getLength() + self.l2.getLength() \
            + self.l3.getLength()


# @TODO Test classes
def main():
    p1 = Point(0, 0)
    p2 = Point(0, 4)
    p3 = Point(3, 0)

    print("distance p1 from p2")
    print(p2.distanceFrom(p1))

    # test class Line
    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p3, p1)
    print('Length of L1:', l1.getLength())
    triangle = Triangle(l1, l2, l3)
    print('Triangle:', triangle.getPerimeter())


if __name__ == "__main__":
    # test class point
    main()


class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def getPoints(self):
        return x,y

    def distanceFrom(self,p2):
        return ((self.x-p2.x)**2+(self.y-p2.y)**2)**0.5

    def __repr__(self):
        return f"[{self.x},{self.y}]"



class Line:
    def __init__(self, p1,p2):
        self.p1 = p1
        self.p2 = p2

    def getLength(self):
        return self.p1.distanceFrom(self.p2)

    def __repr__(self):
        return f"from [{self.p1.x},{self.p1.y}] to [{self.p2.x},{self.p2.y}] with length {self.getLength()}"


class Triangle:
    def __init__(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def getPerimeter(self):
        return self.l1.getLength()+self.l2.getLength()+self.l3.getLength()

    def getArea(self):
        a,b,c = l1.getLength(),l2.getLength(),l3.getLength()
        print(a)
        sin_angle = ((2*b*c)**2-(b**2+c**2-a**2)**2)**0.5/(2*b*c)
        return 0.5*b*c*sin_angle

    def __repr__(self):
        return f"Triangle with lengths [{self.l1.getLength()}, {self.l2.getLength()}, {self.l3.getLength()}]"

if __name__=="__main__":
    # Points
    p1 = Point(0,0)
    p2 = Point(2,0)
    p3 = Point(0,2)
    print("Points")
    print(p1)
    print(p2)
    print(p3)

    # Lines
    l1 = Line(p1,p2)
    l2 = Line(p2,p3)
    l3 = Line(p1,p3)
    print("Lines")
    print(l1)
    print(l2)
    print(l3)

    # triangle
    triangle = Triangle(l1,l2,l3)
    print(triangle)
    print("Perimeter:", triangle.getPerimeter())
    print("Area:", triangle.getArea())

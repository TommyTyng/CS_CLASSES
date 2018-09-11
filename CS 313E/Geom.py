#  File: Geom.py

#  Description:

#  Student Name: Andrew Han

#  Student UT EID: ah49372

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created:

#  Date Last Modified:

import math


class Point(object):
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
    # constructor
    def __init__(self, radius=1, x=0, y=0):
        self.radius = radius
        self.center = Point(x, y)

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c intersects this circle (non-zero area of overlap)
    def does_intersect(self, c):
        distance = self.center.dist(c.center)
        return (distance < (self.radius + c.radius))

    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    def circle_circumscribes(self, r):
        x = (r.ul.x + r.lr.x) / 2
        y = (r.lr.y + r.ul.y) / 2
        center = Point(x, y)
        radius = center.dist(r.ul)
        new_Circle = Circle(radius, x, y)
        return new_Circle

    # string representation of a circle
    def __str__(self):
        return 'Radius: ' + str(self.radius) + ', Center: ' + str(self.center)

    # test for equality of radius
    def __eq__(self, other):
        tol = 1.0e-16
        return (abs(self.radius - other.radius < tol) and abs(self.radius - other.radius < tol))


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    def length(self):
        return (self.lr.x - self.ul.x)

    # determine width of Rectangle (distance along the y axis)
    def width(self):
        return (self.ul.y - self.lr.y)

    # determine the perimeter
    def perimeter(self):
        return 2 * (self.length() + self.width())

    # determine the area
    def area(self):
        return self.length() * self.width()

    # determine if a point is strictly inside the Rectangle
    def point_inside(self, p):
        if (p.x >= min(self.ul.x, self.lr.x)) and (p.x <= max(self.ul.x, self.lr.x)) and (
            p.y >= min(self.ul.y, self.lr.y)) and (p.y <= max(self.ul.y, self.lr.y)):
            return True
        else:
            return False

    # determine if another Rectangle is strictly inside this Rectangle
    def rectangle_inside(self, r):
        if ((self.ul.y >= r.ul.y and self.lr.y <= r.lr.y) and (self.lr.x >= r.lr.x and self.ul.x <= r.ul.x)):
            return True

    # determine if two Rectangles overlap (non-zero area of overlap)
    def does_intersect(self, other):
        if (self.ul.x > other.lr.x) and (other.lr.x > self.ul.x):
            return False
        elif (self.ul.y < other.lr.y) and (other.lr.y < self.ul.y):
            return False
        else:
            return True

    # determine the smallest rectangle that circumscribes a circle
    # sides of the rectangle are tangents to circle c
    def rect_circumscribe(self,c):
        ul_x = c.center.x - c.radius
        ul_y = c.center.y + c.radius
        lr_x = c.center.x + c.radius
        lr_y = c.center.y - c.radius
        new_rect = Rectangle(ul_x, ul_y, lr_x, lr_y)
        return new_rect

    # give string representation of a rectangle
    def __str__(self):
        return "Length: " + str(self.length()) + "Width: " + str(self.width())

    # determine if two rectangles have the same length and width
    def __eq__(self, other):
        tol = 1.0e-16
        return (abs(self.length() - other.length() < tol) and abs(self.length() - other.length() < tol))


def main():
    # open the file geom.txt
    inFile = open('geom.txt', 'r')

    # create Point objects P and Q
    inFile_p = inFile.readline()
    inFile_p = inFile_p.strip()
    inFile_p = inFile_p.split()
    p1_x = float(inFile_p[0])
    p1_y = float(inFile_p[1])
    inFile_p = Point(p1_x, p1_y)

    inFile_q = inFile.readline()
    inFile_q = inFile_q.strip()
    inFile_q = inFile_q.split()
    q1_x = float(inFile_q[0])
    q1_y = float(inFile_q[1])
    inFile_q = Point(q1_x, q1_y)

    # print the coordinates of the points P and Q
    print('Coordinates of P:', inFile_p)
    print('Coordinates of Q:', inFile_q)

    # find the distance between the points P and Q
    distance = inFile_p.dist(inFile_q)
    print('Distance between P and Q: ', distance)

    # create two Circle objects C and D
    inFile_circC = inFile.readline()
    inFile_circC = inFile_circC.strip()
    inFile_circC = inFile_circC.split()
    radius1 = float(inFile_circC[2])
    c1_x = float(inFile_circC[0])
    c1_y = float(inFile_circC[1])
    inFile_circC = Circle(radius1, c1_x, c1_y)

    inFile_circD = inFile.readline()
    inFile_circD = inFile_circD.strip()
    inFile_circD = inFile_circD.split()
    radius2 = float(inFile_circD[2])
    d1_x = float(inFile_circD[0])
    d1_y = float(inFile_circD[1])
    inFile_circD = Circle(radius2, d1_x, d1_y)
    # print C and D
    print("CircleC:" + str(inFile_circC))
    print("CircleD:" + str(inFile_circD))
    # compute the circumference of C
    circumC = Circle.circumference(inFile_circC)
    print("Circumference of C:", circumC)
    # compute the area of D
    areaD = Circle.area(inFile_circD)
    print("Area of D: ", areaD)

    # determine if P is strictly inside C
    if inFile_circC.point_inside(inFile_p):
        print("P is inside C")
    else:
        print("P is not inside C")

    # determine if C is strictly inside D
    if inFile_circD.circle_inside(inFile_circC):
        print("C is inside D")
    else:
        print("C is not inside D")

    # determine if C and D intersect (non zero area of intersection)
    if inFile_circD.does_intersect(inFile_circC):
        print("C does intersect D")
    else:
        print("C does not intersect D")

    # determine if C and D are equal (have the same radius)
    if (Circle.circumference(inFile_circC) == Circle.circumference(inFile_circD)) and (
        Circle.area(inFile_circC) == Circle.area(inFile_circD)):
        print("C is equal to D")
    else:
        print("C is not equal to D")

    # create two rectangle objects G and H
    inFile_rectG = inFile.readline()
    inFile_rectG = inFile_rectG.strip()
    inFile_rectG = inFile_rectG.split()
    ul_x1 = float(inFile_rectG[0])
    ul_y1 = float(inFile_rectG[1])
    lr_x1 = float(inFile_rectG[2])
    lr_y1 = float(inFile_rectG[3])
    inFile_rectG = Rectangle(ul_x1, ul_y1, lr_x1, lr_y1)

    inFile_rectH = inFile.readline()
    inFile_rectH = inFile_rectH.strip()
    inFile_rectH = inFile_rectH.split()
    ul_x2 = float(inFile_rectH[0])
    ul_y2 = float(inFile_rectH[1])
    lr_x2 = float(inFile_rectH[2])
    lr_y2 = float(inFile_rectH[3])
    inFile_rectH = Rectangle(ul_x2, ul_y2, lr_x2, lr_y2)

    # print the two rectangles G and H
    print("Rectangle G: ", str(inFile_rectG))
    print("Rectangle H: ", str(inFile_rectH))

    # determine the length of G (distance along x axis)
    lengG = Rectangle.length(inFile_rectG)
    print("Length of G: ", lengG)
    # determine the width of H (distance along y axis)
    widH = Rectangle.width(inFile_rectH)
    print("Width of H: ", widH)

    # determine the perimeter of G
    perimG = Rectangle.perimeter(inFile_rectG)
    print("Perimeter of G: ", perimG)

    # determine the area of H
    areaH = Rectangle.area(inFile_rectH)
    print("Area of H: ", areaH)

    # determine if point P is strictly inside rectangle G
    if inFile_rectG.point_inside(inFile_p):
        print("P is inside G")
    else:
        print("P is not inside G")

    # determine if rectangle G is strictly inside rectangle H
    if inFile_rectH.rectangle_inside(inFile_rectG):
        print("G is inside H")
    else:
        print("G is not inside H")
    # determine if rectangles G and H overlap (non-zero area of overlap)
    if inFile_rectH.does_intersect(inFile_rectG):
        print("G does overlap H")
    else:
        print("G does not overlap H")

    # find the smallest circle that circumscribes rectangle G
    # goes through the four vertices of the rectangle
    new_circle = 0
    if Circle.circle_circumscribes(new_circle,inFile_rectG):
        print("Circle that circumscribes G: ", new_circle)
    else:
        print('Circle that circumscribes G: None')

    # find the smallest rectangle that circumscribes circle D
    # all four sides of the rectangle are tangents to the circle
    new_rect = ''
    if Rectangle.rect_circumscribe(new_rect,inFile_circD):
        print("Rectangle that circumscribes D: ", new_rect)
    else:
        print('"Rectangle that circumscribes D: None')

    #determine if the two rectangles have the same length and width
    if (Rectangle.length(inFile_rectG) == Rectangle.length(inFile_rectH)) and (Rectangle.width(inFile_rectG) == Rectangle.width(inFile_rectH)):
        print("Rectangle G is equal to H")
    else:
        print("Rectangle G is not equal to H")

    # close the file geom.txt
    inFile.close()


main()
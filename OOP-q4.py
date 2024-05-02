# Write a Python program to create a class that represents a shape. 
# Include methods to calculate its area and perimeter. 
# Implement subclasses for different shapes like circle, triangle, and square.

import math

class Shape:

    def __init__(self):
        # empty constructor
        pass

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (r ** 2)

    def perimeter(self):
        return math.pi * r * 2

class Rectangle(Shape):

    def __init__(self, h, w):
        self.h = h
        self.w = w

    def area(self):
        return self.h * self.w

    def perimeter(self):
        return (2 * self.h) + (2 * self.w)

class Triange(Shape):

    def __init__(self, b, h, s1, s2, s3):
        self.b = b
        self.h = h
        self.s1 = s1
        self.s2 = s2
        self.s3 = self.s3

    def area(self):
        return 0.5 * self.b * self.h

    def perimeter(self):
        return self.s1 + self.s2 + self.s3

r = 5
cirle_obj = Circle(5)
print(cirle_obj.area())
print(cirle_obj.perimeter())

l = 10
d = 20
rect_obj =  Rectangle(l, d)
print(rect_obj.area())
print(rect_obj.perimeter())

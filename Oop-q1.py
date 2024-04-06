# Write a Python program to create a class representing a Circle. 
# Include methods to calculate its area and perimeter.

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = pi * self.radius**2
        return a

    def perimeter(self):
        p = 2 * pi * self.radius
        return p

test_circle = Circle(5)
print(f'AREA:\t {test_circle.area()}')
print(f'PERIMETER:\t {test_circle.perimeter()}')

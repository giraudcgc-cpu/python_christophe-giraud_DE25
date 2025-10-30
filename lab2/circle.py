from shape import Shapes
import matplotlib.pyplot as plt
import math     #error: did not know, had to import math, so math.pi was not defined
# import math found at https://www.w3schools.com/python/ref_math_pi.asp
# https://www.youtube.com/watch?v=T8RXMRlRoRg

class Circle(Shapes):   #inheritance
        def __init__(self, x=0, y=0, radius=1) -> int|float: #radius must be minimum 1, "by default"
            super().__init__(x, y)
            if not isinstance(radius, float|int):
                raise TypeError(f"Radius must be a number, integer or float")
            if radius <= 0:
                raise ValueError(f"Radius must be a positive number as length is positive")
            self._radius = radius      

@property
def radius(self):
    self._radius = radius

# here will overide parent Shapes
@property
def area(self):
    return f"Area = {math.pi} * {self._radius} ** 2"  # took pie from https://www.w3schools.com/python/ref_math_pi.asp

# overides 
@property
def perimeter(self):
    return f"Perimeter = {math.pi} * {self._radius} * 2"
              
def is_a_unit_circle(self) -> bool:
    if self._radius != 1 or self._x != 0 or self._y != 0:
        return False
    else:
        return True

#overides
def __eq__(self, other):
    if not isinstance(other, type(self)):
        return False
    if self._radius == other._radius:   # error: had 0 instead of ==
        return True
    
#overides
def __repr__(self):
    return f"Circle, radius= {self._radius}, center at x={self._x}, y={self._y}"

#overides
def __str__(self):
    return f"This circle has center coordinates x={self._x}, y={self._y} and a radius of {self._radius}"

#overides
# matplotlib https://www.geeksforgeeks.org/python/how-to-draw-a-circle-using-matplotlib-in-python/
def draw(self):
    fig, ax = plt.subplots()
# Circle(xy, radius, color, ...)
    circle = plt.Circle((self.x, self.y), radius, color='red', fill=False)
# Add the circle to the axes
    ax.add_patch(circle)
# Ensure the circle is not distorted (x and y axes have the same scale)
    ax.set_aspect('equal', adjustable='box')
# Display
    plt.show()
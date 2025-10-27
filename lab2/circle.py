from shape_parent_base import Shapes
#import math foundd at https://www.w3schools.com/python/ref_math_pi.asp
#drawing, how?

class Circle(Shapes):
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
    if self._radius = other._radius:
        return True
    
#overides
def __repr__(self):
    return f"Circle, radius= {self._radius}, center at x={self._x}, y={self._y}"

#overides
def __str__(self):
    return f"This circle has center coordinates x={self._x}, y={self._y} and a radius of {self._radius}"

# ???drawing
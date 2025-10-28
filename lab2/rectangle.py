from shape_parent_base import Shapes
import matplotlib.pyplot as plt
import math 
# Imported all like for circle.py

class Rectangle(Shapes):
    def __init__(self, width: int|float, height: int|float, x=0, y=0):
        super().__init__(x, y)
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("width and height must be positive numbers, integer or float")
        if width or height <= 0:
            raise ValueError("Enter a positive number greater than 0")
        self._width = width
        self._heigth = height

@property
def width(self):
    return self._width

@property
def height(self):
    return self._height

#overides
@property
def area(self):
    return self._width * self._height

#overides
@property
def perimeter(self):
    return 2 * (self._width + self._height)



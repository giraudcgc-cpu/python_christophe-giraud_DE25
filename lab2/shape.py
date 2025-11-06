# Here I will be defining the Shape class, parent of the 2 classes: Circle and Rectangle.
# I will, as much as possible, include the common behaviours/actions
# think about documentation

from utils import validate_number
from numbers import Number
from typing import Any

class Shape:
    def __init__(self, x: int|float, y: int|float) -> None:        
        self.x = x
        self.y = y 
    

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        validate_number(value)
        self._x = value
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        validate_number(value)
        self._y = value
        

    def area(self):
        raise NotImplemented # defined in children classes

    def perimeter_is(self):  # the same here         
        raise NotImplemented


    def __eq__(self, other): # or just pass?
        if not isinstance(other, Shape): 
            return False
        return self._x == other._x and self._y == other._y 
    
    # oblige to drop function here as I had error that function was not define as too low in the code
    def _area_of(self, other: Any) -> float: #Had it in utils but circular import issue so, moved it here, private so nobody calls it, only used here
        if isinstance(other, Shape):
            return other.area
        if isinstance(other, Number):
            return float(other)   # in matplotlib int become float, will need it for pi. keep it simple, otherwise need to use Union[]
        return NotImplemented

    def __ge__(self, other): # >= Greater than or equal to 
        return self.area >= self._area_of(other)
    
    def __le__(self, other):   # <= Less than or equal to
        return self.area <=  self._area_of(other)

    def __gt__(self, other): 
        return self.area > self._area_of(other)
    
    def __lt__(self, other):
        return self.area < self._area_of(other)
        

# moving figures with translate()
    def translate(self, x2:float|int, y2:float|int):
        validate_number(x2)
        validate_number(y2)
        self._x += x2
        self._y += y2
        return f"moves its center {x2} points in x and {y2} points in y. New center:({self._x},{self._y})"

# to be overidden in both children
    def __repr__(self):
        return f"shape{type(self)}, center (x={self._x}, y={self._y})"

    def __str__(self):
        return f"This represents a {type(self).__name__}. Its center coordinates are x={self._x} and y={self._y}"

#BELOW IS FOR DRAW - MAYBE
# matplotlib: googled how to create a circle with matplotlib python
# https://www.geeksforgeeks.org/python/how-to-draw-a-circle-using-matplotlib-in-python/

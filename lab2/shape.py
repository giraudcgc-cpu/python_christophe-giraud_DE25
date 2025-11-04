# Here I will be defining the Shape class, parent of the 2 classes: Circle and Rectangle.
# I will, as much as possible, include the common behaviours/actions
# think about documentation

import matplotlib.pyplot as plt

class Shape:
    def __init__(self, x: int|float, y: int|float) -> None:        
        self.x = x
        self.y = y 
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        if value is None:
            raise ValueError("Missing x value! You need to enter the x value!")
        if not isinstance(value, (int, float)):
            raise TypeError(f"{value!r} is invalid. Center coordinate x must be a number, int or float, not {type(value).__name__}")
        if value < 0:
            raise ValueError(f"Value cannot be less than zero 0")  
        self._x = value
        
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        if value is None:
            raise ValueError("Missing y value! You need to enter the y value!")
        if not isinstance(value, (int, float)):
            raise TypeError(f"{value!r} is invalid. Center coordinate y must be a number, int or float, not {type(value).__name__}")
        if value < 0:
            raise ValueError(f"Value cannot be less than zero 0")  #ask Kokchun if we auhtorize negative numbers
        self._y = value
        

    def area(self):
        raise NotImplemented # defined in children classes

    def perimeter_is(self):  # the same here         
        raise NotImplemented


    def __eq__(self, other): # or just pass?
        if not isinstance(other, Shape): # if other is not the same type as self (circle or rectangle)
            return False
        return self._x == other._x and self._y == other._y 

    def __ge__(self, other): # >= Greater than or equal to 
        if isinstance(other, Shape): 
            return self.area >= other.area
        if isinstance(other(float, int)):
            return self.area >= other.area
        return NotImplemented

    def __le__(self, other):   # <= Less than or equal to
        if isinstance(other, type(Shape)):
            return self.area <=  other.area
        if isinstance(other, (int, float)):
            return self.area <=  other.area
        return NotImplemented

    def __gt__(self, other): 
        if isinstance(other, Shape):
            return self.area > other.area
        if isinstance(other, (int, float)):
            return self.area > other
        return NotImplemented
    
    
    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.area < other.area
        if isinstance(other, (float, int)):
            return self.area < other.area
        return NotImplemented
       

# moving figures with translate()
    def translate(self, x2:float|int, y2:float|int):
        if not isinstance(x2, (int|float)):
            raise TypeError(f"{x2!r} is not valid. Please enter valid input: integer or float, not {type(x2).__name__}")
        if not isinstance(y2, (int|float)):
            raise TypeError(f"{y2!r} is not valid. Please enter valid input: integer or float, not {type(y2).__name__}")
        self._x += x2
        self._y += y2
        return f"moves its center {x2} points in x and {y2} points in y. New center:({self._x},{self._y})"

# to be overidden in both children
    def __repr__(self):
        return f"shape:{type(self)}, center (x={self._x}, y={self._y})"

    def __str__(self):
        return f"This represents a {type(self).__name__}. Its center coordinates are x={self._x} and y={self._y}"

# matplotlib: googled how to create a circle with matplotlib python
# https://www.geeksforgeeks.org/python/how-to-draw-a-circle-using-matplotlib-in-python/
# ??? can it be just "pass" here instead of several lines of code to overide in the children??? 
    def draw(self):
        pass
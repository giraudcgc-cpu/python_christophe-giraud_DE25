# Here I will be defining the Shape class, parent of the 2 classes: Circle and Rectangle.
# I will, as much as possible, include the common behaviours/actions
# think about documentation

import matplotlib.pyplot as plt

class Shape:
    def __init__(self, x: int|float, y: int|float) -> None:         #error: had "sself"
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numbers")
        self._x = x
        self._y = y 

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    @property #defined the center
    def center(self):
        return (self._x, self._y)

    @center.setter 
    def center(self, value):
        self._x, self._y = value

    def area(self) -> float|int:
        raise NotImplementedError # defined in rectangle and circle separated files

    def perimeter_is(self):       # the same here         
        raise NotImplementedError


    def __eq__(self, other): # or just pass?
        if not isinstance(other, Shape): # if other is not the same type as self (circle or rectangle)
            return False
        return self._x == other._x and self._y == other._y 

    def __ge__(self, other): # >= Greater than or equal to 
        if not isinstance(other, Shape): # if other is not a type of shape
            return f"NEED TO DEFINE ERROR MESSAGE 1"
        return self.area <= other.area

    def __le__(self, other):   # <= Less than or equal to
        if not isinstance(other, type(Shape)):
            return f"NEED TO DEFINE ERROR MESSAGE 2"
        return #??? <= perimeter_is???

    def __gt__(self, other): 
        if isinstance(other, Shape):
            return self.area > other.area
        if isinstance(other, (int, float)):
            return self.area > other
        return NotImplemented
    

    # def perimeter to do

    #def __lt__(self, other): 
     #   if not isinstance(other, Shape):
     #       return f"NEED TO DEFINE ERROR MESSAGE 3"
     #   return self.area < other.area # for comparing Shape based on their areas
    
    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.area < other.area
        if isinstance(other, (float, int)):
            return self.area < other.area
        return NotImplemented
       

# moving figures with translate()
    def translate(self, x2:float|int, y2:float|int):
        if not isinstance(x2, (int|float)) or not isinstance(y2, (int|float)):
            raise TypeError("Please enter valid input: integer or float")
        self._x += x2
        self._y += y2

# to be overidden in both children
    def __repr__(self):
        return f"shape:{type(self)}, center (x={self._x}, y={self._y})"

    def __str__(self):
        return f"This represents a {type()}. Its center coordinates are x={self._x} and y={self._y}"

# matplotlib: googled how to create a circle with matplotlib python
# https://www.geeksforgeeks.org/python/how-to-draw-a-circle-using-matplotlib-in-python/
# ??? can it be just "pass" here instead of several lines of code to overide in the children??? 
    def draw(self):
        pass
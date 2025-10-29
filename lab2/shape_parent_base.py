# Here I will be defining the SHAPES class, parent of the 2 classes: Circle and Rectangle.
# I will, as much as possible, include the common behaviours/actions
# Remember: need to import stuff!!!

import matplotlib.pyplot as plt

class Shapes:
    def __init__(self, x: int|float = 0, y: int|float = 0) -> None: #error: had "sself"
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be integer or float")
        self._x = x
        self._y = y 
# _x and _y are marked private, should only be modified through translate() 


@property
def x(self):
    return self._x

@property
def y(self):
    return self._y

# area or perimeter here as "common operations" AND  under the children as split perimeter/area for both + overide ???
def area(self):
    self.are = area
    pass

def perimeter(self):
    self.perimeter = perimeter
    pass


def __eq__(self, other):
    if not isinstance(other, type(self)): # if other is not the same type as self (circle or rectangle)
        return False
    return self._x == other._x and self._y == other._y 

def __ge__(self, other): # >= Greater than or equal to ???comparing areas or perimeter?
    if not isinstance(other, type(Shapes)): # if other is not a type of shape
        return f"You cannot compare apples and oranges!"
    return #??? not sure >=

def __le__(self, other):   # <= Less than or equal to
    if not isinstance(other, type(Shapes)):
        return f"You cannot compare apples and oranges"
    return #??? <= size/area to compare???

def __gt__(self, other): 
    if not isinstance(other, type(Shapes)):
        return f"You cannot compare apples and oranges"
    return # self.area > other.area or self.periimeter > other.perimeter ???

def __lt__(self, other):
    if not isinstance(other, type(Shapes)):
        return f"You cannot compare apples and oranges"
    return # self.area < other.area or .perimeter ???

# moving figures with translate()
def translate(self, x2, y2):
    if not isinstance(x2, int|float) or not isinstance(y2, int|float):
        raise TypeError("Please enter valid input: integer or float")
    self._x = x2
    self._y = y2

# to be overidden in both children
def __repr__(self):
    return f"shape:{type(self)}, with center coordinates at (x={self._x}, y={self._y})"

def __str__(self):
    return f"This represents a {type()}. Its center coordinates are x={self._x} and y={self._y}"

# matplotlib: googled how to create a circle with matplotlib python
# or https://www.geeksforgeeks.org/python/how-to-draw-a-circle-using-matplotlib-in-python/

# ??? can it be just "pass" here instead of several lines of code to overide in the children???
# def draw(self):
#    pass 
def draw(self):
    fig, ax = plt.subplots()
    ax.set.aspect('equal')
    ax.set_xlim(self._x - 5, self._x + 5)  #random and small to test
    ax.set_ylim(self._y - 5, self._y + 5)
    plt.show()










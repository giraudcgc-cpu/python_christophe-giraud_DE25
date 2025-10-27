# Here I will be defining the SHAPES class, parent of the 2 classes: Circle and Rectangle.
# I will, as much as possible, include the common behaviours/actions
# Remember: need to import stuff!!!


class Shapes:
    def __init__(self, x = 0, y = 0) -> int|float: # starting point
        if x or y not isinstance or != int|float:
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

# area or perimeter here as "common operations" or under the children as split perimeter/area?
#def area(self):
#    self.are = area
#    pass
#def perimeter(self):
#    self.perimeter = perimeter
#    pass


def __eq__(self, other):
    if not isinstance(other, type(self)): # if other is not the same type as self (circle or rectangle)
        return False
    return self._x = other._x and self._y = other._y 

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





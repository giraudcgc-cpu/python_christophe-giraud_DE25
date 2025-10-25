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

#area and perimeter
#get all the methods(), drawing?
        
        
    
# Here I will be defining the Shape class, parent of the 2 classes: Circle and Rectangle.
# I will, as much as possible, include the common behaviours/actions
# think about documentation

from utils import validate_number
from numbers import Number
from typing import Any

class Shape:
    def __init__(self, x: Number, y: Number) -> None:        
        self.x = x
        self.y = y 
    
    @property
    def x(self) -> Number:
        return self._x
    
    @x.setter
    def x(self, value) -> Number:
        validate_number(value)
        self._x = value
        
    @property
    def y(self) -> Number:
        return self._y
    
    @y.setter
    def y(self, value) -> Number:
        validate_number(value)
        self._y = value

    # defined in children classes   
    def area(self): 
        raise NotImplementedError 

    # defined in children classes
    def perimeter_is(self):          
        raise NotImplementedError

    def __eq__(self, other): 
        raise NotImplementedError
    
    #Had it in utils but circular import issue so, moved it here, private so nobody calls it, only used here
    def _area_of(self, other: Any) -> float: 
        if isinstance(other, Shape):
            return other.area
        if isinstance(other, Number):
            # in matplotlib int become float, will need it for pi
            return float(other)   
        raise TypeError(f"Invalid comparison of types. Cannot compare {type(self).__name__} with {type(other).__name__}")


    def __ge__(self, other) -> Number:  
        return self.area >= self._area_of(other)
    
    def __le__(self, other) -> Number:   
        return self.area <=  self._area_of(other)

    def __gt__(self, other) -> Number: 
        return self.area > self._area_of(other)
    
    def __lt__(self, other) -> Number:
        return self.area < self._area_of(other)

    def translate(self, x2:Number, y2:Number): 
        # validate_number(x2)
        # validate_number(y2)
        self.x = self.x + x2
        self.y = self.y + y2
        return self
        # return f"moves its center {x2} points in x and {y2} points in y. New center:({self._x},{self._y})"


    # overidden in both children classes
    def __repr__(self): 
        return f"{type(self).__name__}(center x={self._x}, y={self._y})"

    # overriden in both children classes
    def __str__(self):
        raise NotImplementedError


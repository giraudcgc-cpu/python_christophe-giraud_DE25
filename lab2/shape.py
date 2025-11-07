
# think about documentation

from utils import validate_number
from numbers import Number
from typing import Any

class Shape:
    def __init__(self, x: Number, y: Number, name=None) -> None:        
        self.x = x
        self.y = y 
        self.name = name
    
    @property
    def x(self) -> Number:
        return self._x
    
    @x.setter
    def x(self, value) -> Number:
        if isinstance(value, bool):
            raise TypeError(f"Invalid {type(value).__name__}, length must be a positive number, int or float")
        validate_number(value)
        self._x = value
        
    @property
    def y(self) -> Number:
        return self._y
    
    @y.setter
    def y(self, value) -> Number:
        if isinstance(value, bool):
            raise TypeError(f"Invalid {type(value).__name__}, length must be a positive number, int or float")
        validate_number(value)
        self._y = value

    # defined in children classes / are read-only
    @property  
    def area(self) -> Number: 
        raise NotImplementedError("Children classes will define area")

    # defined in children classes
    def perimeter_is(self) -> Number:          
        raise NotImplementedError("Children classes will implement")
    
    #First I had them in circle and had forgoten Rectangle
    # with my compare_with makes sense to have it for both (here)
    @property
    def area_rounded(self) -> Number:
        return round(self.area, 2)

    @property
    def perimeter_rounded(self) -> Number:  
        return round(self.perimeter_is, 2)

    def __eq__(self, other): 
        raise NotImplementedError
    
    #Had it in utils but circular import issue so, moved it here, private so nobody calls it, only used here
    def _area_of(self, other: Any) -> float: 
        if isinstance(other, Shape):
            return other.area
        if isinstance(other, bool):
            raise TypeError(f"Invalid comparison {type(self).__name__} with boolean")
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
        if isinstance(x2, bool):
            raise TypeError(f"Invalid {type(x2).__name__}, x2 must be a number, int or float")
        if isinstance(y2, bool):
            raise TypeError(f"Invalid {type(y2).__name__}, y2 must be a number, int or float")
        validate_number(x2)
        validate_number(y2)
        self.x = self.x + x2
        self.y = self.y + y2
        return self
        #return f"moves its center {x2} points in x and {y2} points in y. New center:({self._x},{self._y})"

    def _get_the_name(self):
        if self.name:
            return self.name
        return type(self).__name__
        
    def compare_with(self, other: Any) -> str:
        # __eq__ in the children classes compares the dimensions, here comparing, shapes, area, perimeter
        if not isinstance(other, Shape):
            if isinstance(other, bool):
                raise TypeError(f"Invalid comparison {type(self).__name__} with boolean")
            if isinstance(other, Number):
                return (f"Comparison between {type(self).__name__} and value {other}."
                f"{self._get_the_name()} has an area of {self.area_rounded}."
                f"The value is {other}")
            raise TypeError(f"{type(self).__name__} cannot be compare with {type(other).__name__}")
        
        self_name = self._get_the_name()
        other_name = other._get_the_name()

        #if isinstance(other,Shape):
        same_type = type(self) == type(other)
        same_or_not = "Same type!" if same_type else "Different types!"
        
        lines = [
        f"They are {same_or_not}",
        f"The first one ({self_name}) area is {self.area_rounded} and perimeter is {self.perimeter_rounded}",
        f"The second one ({other_name}) area is {other.area_rounded} and perimeter is {other.perimeter_rounded}",
        ]

        return "\n".join(lines)


    # overidden in both children classes
    def __repr__(self): 
        return f"{type(self).__name__}(center x={self._x}, y={self._y})"

    # overriden in both children classes
    def __str__(self):
        raise NotImplementedError


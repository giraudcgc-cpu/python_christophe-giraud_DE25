from shape import Shape
import math 
from utils import validate_number, validate_positive # !!! no import of _area_of here = to delete
from numbers import Number

class Circle(Shape):   
    def __init__(self, x:Number=0, y:Number=0, radius:Number=0) -> None: 
        super().__init__(x, y)

        if  isinstance (radius, bool):
            raise TypeError(f"Invalid {type(radius).__name__}, radius must be a positive number, int or float")
        
        self.radius = radius      

    @property
    def radius(self) -> Number:
        return self._radius

    @radius.setter
    def radius(self, value) -> Number:  
        validate_number(value)
        validate_positive(value, "radius")
        self._radius = value

    # overrides parent class
    @property
    def area(self) -> Number:
        return math.pi * (self._radius ** 2)
    
    @property
    def area_rounded(self) -> Number:
        return round(self.area, 2)

    # overrides parent class
    @property
    def perimeter_is(self) -> Number:
        return math.pi * self._radius * 2
    
    @property
    def perimeter_rounded(self) -> Number:  
        return round(self.perimeter_is, 2)
              
    def unit_circle(self) -> bool:
        return self._radius == 1 and self._x == 0 and self._y == 0

    # overrides if same radius, they have same area and same perimeter. ignoring center postion
    def __eq__(self, other) -> bool:
        if not isinstance(other, Circle):
            return False
        # To be equal, same center and radius
        return self._radius == other._radius    
    
    # overrides parent class
    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self._x}, y={self._y}, radius={self._radius})"

    # overrides parent class
    def __str__(self) -> str:
        return f"This circle has center coordinates x={self._x}, y={self._y} and a radius of {self._radius}"



from shape import Shape
import math
from utils import validate_positive, validate_number # !!! no import of _area_of here
from numbers import Number


class Rectangle(Shape):
    def __init__(self, x: Number, y:Number, length: Number, width: Number):     
        super().__init__(x, y)
        self.length = length
        self.width = width

    @property
    def length(self) -> Number:
        return self._length
    
    @length.setter
    def length(self, value) -> Number: 
        validate_number(value)
        validate_positive(value, "length")
        self._length = value
        
    @property
    def width(self) -> Number:
        return self._width
    
    @width.setter
    def width(self, value) -> Number:
        validate_number(value)
        validate_positive(value, "width")
        self._width = value

    # overrides parent class
    @property
    def area(self) -> Number:
        return self._length * self._width

    # overrides parent class
    @property
    def perimeter_is(self) -> Number:
        return 2 * (self._length + self._width)
    
    def is_square(self) -> bool:                        
        return self.length == self.width
                
    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y}, length={self._length}, width={self._width})"

    def __str__(self) -> str:
        return f"Point ({self.x}, {self.y}) is the center of the rectangle with length {self._length} and width {self._width}"

    def __eq__(self, other)-> bool:
        if not isinstance(other, Rectangle):
            return False
        # inclination is not a problem
        if self._length == other._length and self._width == other._width:
            return True
        if self._length == other._width and self._width == other._length:
            return True
        return False
         
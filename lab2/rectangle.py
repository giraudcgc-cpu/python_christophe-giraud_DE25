
from shape import Shape
import math
from utils import validate_positive, validate_number 
from numbers import Number


class Rectangle(Shape):
    """ 
    Rectangle inherits from Shape (parent class).

    The centre is determined by: x,y
    x and y can be negative, length and width must be positive
    Values are validated and encapsulated like _length and _width

    Unique to Rectangle: is_square 
    
    Few inherited methods or attributes from Shape:
    1.position and movement
    - .x, .y (with validation & encapsulation)
    - .translate(x2, y2) moves the centre point

    2.Area & perimeter (ready to use)
    - .area_rounded -> area rounded to 2 decimals
    - .perimeter_rounded -> perimeter rounded

    3.Comparisons by area only
    - with: >, <, >=, <=  they can compare any two shapes by area
    
    4."Extra" comparison with compare_with:
    - returns a string with:
        • indication of similar or different type/shape
        • rounded area and perimeter for both
    
    5.repr and str (but override them)
    - __repr__ shows center + size 
    - __str__  for nice text

    Examples usage:
    r1 = Rectangle(1, 2, 4, 3) 
    r1.x = 10 
    r1  which prints: Rectangle(x=10, y=2, length=4, width=3)
    
    r1 = Rectangle(1, 2, 4, 3)
    r1.y = True   which prints: TypeError: Invalid bool, length must be a positive number, int or float

    c1 = Circle(0, 0, 3) 
    print(r1.compare_with(c1))
    which prints:
    They are Different types!
    The first one (Rectangle) area is 12 and perimeter is 14
    The second one (Circle) area is 28.27 and perimeter is 18.85"""

    def __init__(self, x: Number, y:Number, length: Number, width: Number) -> None: 
        """Create rectangle with obligatory: center at coordinate (x, y) with length and width
        x and y can be negative, not length and width, validation via setters (no bool and > 0)"""    
        super().__init__(x, y)
        self.length = length
        self.width = width

    # define length property getter
    @property
    def length(self) -> Number:
        """Length of rectangle is private and stored as _length"""
        return self._length
    
    # define setter method for length / validation / raise error
    @length.setter
    def length(self, value) -> None: 
        """Set length must be number > 0 (no bool)
        Excluded first bool as used Number in validate_number in utils that I import"""
        if isinstance(value, bool):
            raise TypeError(f"Invalid {type(value).__name__}, length must be a positive number, int or float")
        validate_number(value)
        validate_positive(value, "length")
        self._length = value
        
    # define getter width property  
    @property
    def width(self) -> Number:
        """Same logic as for length above"""
        return self._width
    
    # define setter method for width / validation / raise error
    @width.setter
    def width(self, value) -> None:
        """Same logic as for length above"""
        if isinstance(value, bool):
            raise TypeError(f"Invalid {type(value).__name__}, length must be a positive number, int or float")
        validate_number(value)
        validate_positive(value, "width")
        self._width = value

    # overrides parent class
    @property
    def area(self) -> Number:
        return self._length * self._width

    # overrides parent class
    @property
    def perimeter(self) -> Number:
        return 2 * (self._length + self._width)
    
    def is_square(self) -> bool:  
        """Unique for Rectangle"""                      
        return self.length == self.width

    # overrides parent class        
    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x}, y={self.y}, length={self._length}, width={self._width})"

    # overrides parent class
    def __str__(self) -> str:
        return f"Point ({self.x}, {self.y}) is the center of the rectangle with length {self._length} and width {self._width}"

    # overrides parent class
    def __eq__(self, other)-> bool:
        """Equal if same dimensions, length/width can swap"""
        if not isinstance(other, Rectangle):
            return False
        # inclination is not a problem
        if self._length == other._length and self._width == other._width:
            return True
        if self._length == other._width and self._width == other._length:
            return True
        return False
         
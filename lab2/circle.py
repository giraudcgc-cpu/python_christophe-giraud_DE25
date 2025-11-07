from shape import Shape
import math 
from utils import validate_number, validate_positive 
from numbers import Number

class Circle(Shape):
    """
    Circle inherits from Shape (parent class).
    
    The centre is determined by: x,y and the radius.
    
    Values are validated:
    - x and y can be negative, 
    - radius must be positive, not a bool (validated in setter)

    And encapsulated:
    - radius becomes private and is stored as _radius
    - centre is private and stored as _x and _y
    - access only via public .radius, .x, .y
    
    Unique to Circle: is_unit_circle
    
    Otherwise, like Rectangle, same inherited methods or attributes from Shape:
    (only named here, see rectangle.py for the details)
    1.position and movement
    2.Area & perimeter (ready to use)
    3.Comparisons by area only
    4."Extra" comparison with compare_with:
    5.repr and str (but override them)
   
    Like in Rectangle, Circle overrides:
    - area with the formula 
    - perimeter with the formula
    - __str__ shows a nice sentence
    - __eq__ same radius ok, ignoring the centre
    
    Examples usage:
    c1 = Circle(0, 0, 5)   
    c2 = Circle(10, 20, 5)  
    c3 = Circle(0, 0, 3)    
    print(c1 == c2)   prints True  (same radius)
    print(c1 == c3)   prints False (different radius)
    print(c2 == c1)   prints True  (same)

    Circle(0,0,5) == Circle(100,100,5) prints True
    Circle(0,0,5) == Circle(0,0,3)  prints False
    """ 

    def __init__(self, x:Number=0, y:Number=0, radius:Number=0) -> None: 
        """Creates circle with centre (x,y) and radius"""
        super().__init__(x, y)

        if  isinstance (radius, bool):
            raise TypeError(f"Invalid {type(radius).__name__}, radius must be a positive number, int or float")
        
        self.radius = radius  
        """calls setter for validation"""   

    @property
    def radius(self) -> Number:
        """Public, but stored privately as _radius"""
        return self._radius

    @radius.setter
    def radius(self, value) -> None:  
        """Sets radius, only way to change _radius.
        and validates: not bool, a number, > 0, """
        if isinstance(value, bool):
            raise TypeError(f"Invalid {type(value).__name__}, radius must be a positive number, int or float")
        validate_number(value)
        validate_positive(value, "radius")
        self._radius = value

    # overrides parent class
    @property
    def area(self) -> Number:
        return math.pi * (self._radius ** 2)
    
    
    # overrides parent class
    @property
    def perimeter(self) -> Number:
        return math.pi * self._radius * 2
    
                 
    def is_unit_circle(self) -> bool:
        return self._radius == 1 and self._x == 0 and self._y == 0

    def __eq__(self, other) -> bool:
        """Equal if same radius, the centre is ignored
        Same radius --> same area and perimeter"""
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


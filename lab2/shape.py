from utils import validate_number
from numbers import Number
from typing import Any

class Shape:
    """
    Parent class Shape for 2D shapes Circle and Rectange (OOP exercise).

    This exercie covers the OOP fundamentals:
    - Inheritance: Circle and Rectangle inherit from Shape
    - Encapsulation: x and y are private (_x, _y) — use of properties!
    - Polymorphism: same method (area, perimeter) works differently
    - Abstraction: you only see what is important (area, move, compare)

    **This is the base class of Circle and Rectangle which will inherit from it**

    It uses:
    - Inheritance
    - Properties
    - Method overriding
    - Comparison with > and other opertaors overloading
    
    Attributes:
    x (int/float): Center X position
    y (int/float): Center Y position
    name (str or None): Optional name 
    
    Overriden in child classes:
    - area (property)
    - perimeter() (property)
    - __str__()
    - __eq__()

    Rectangle and Circle can:
    - Move via moving their centre coordinates (x,y) with .translate(x2, y2)
    - Compare: >, <, >=, <= (by area), == but also with the method compare_with which compares shape, area and perimeter together
    - Get rounded value when suitable like for area and perimeter with .area_rounded, .perimeter_rounded

    Quick examples:
    c3 = Circle(0, 0, 5)
    c3.area_rounded which prints: 78.54

    c3 = Circle(0, 0, 5)
    c3.translate(3, 4) which prints the repr: Circle(x=3, y=4, radius=5)
    """

    def __init__(self, x: Number, y: Number, name=None) -> None:      
        """Public constructor, creates a new shape
        The real coordinates _x and _y are kept private in the setters.
        Both self.x and self.y call the setters for validation.
        """
        self.x = x
        self.y = y 
        self.name = name
    
    @property
    def x(self) -> Number:
        """Public read-only view of the private x cooridnate"""
        return self._x
    
    @x.setter
    def x(self, value) -> None:
        """Public setter, changes X with validation (encapsulation).
        refuses booleans and non-numeric values (uses validate_number from utils)"""
        if isinstance(value, bool):
            raise TypeError(f"Invalid {type(value).__name__}, length must be a positive number, int or float")
        validate_number(value)
        self._x = value

    # Same logic as for x   
    @property
    def y(self) -> Number:
        return self._y
    
    @y.setter
    def y(self, value) -> None:
        if isinstance(value, bool):
            raise TypeError(f"Invalid {type(value).__name__}, length must be a positive number, int or float")
        validate_number(value)
        self._y = value

    # read-only
    @property  
    def area(self) -> Number: 
        """Area of the shape — To override in Circle/Rectangle!"""
        raise NotImplementedError("Children classes will define area")
    

    # read-only
    @property
    def perimeter(self) -> Number:   
        """Perimeter — To override in child class!"""       
        raise NotImplementedError("Children classes will implement")
    
    
    @property
    def area_rounded(self) -> Number:
        """Encapsulated, rounded area at 2 decimals."""
        return round(self.area, 2)

    @property
    def perimeter_rounded(self) -> Number:  
        """Encapsulated, rounded perimeter at 2 decimals"""
        return round(self.perimeter, 2)

       
    def _area_of(self, other: Any) -> float: 
        """Private helper so nobody calls it, only used here to gets the area of other"""
        if isinstance(other, Shape):
            return other.area
        if isinstance(other, bool):
            raise TypeError(f"Invalid comparison {type(self).__name__} with boolean")
        if isinstance(other, Number):
            # in matplotlib int become float, will need it for pi
            return float(other)   
        raise TypeError(f"Invalid comparison of types. Cannot compare {type(self).__name__} with {type(other).__name__}")

    def __eq__(self, other) -> bool: 
        raise NotImplementedError

    def __ge__(self, other) -> bool: 
        return self.area >= self._area_of(other)
    
    def __le__(self, other)-> bool:   
        return self.area <=  self._area_of(other)

    def __gt__(self, other) -> bool: 
        return self.area > self._area_of(other)
    
    def __lt__(self, other) -> bool:
        return self.area < self._area_of(other)

    def translate(self, x2:Number, y2:Number) -> 'Shape': 
        """Move shape by (x2, y2). Returns self.
        excludes booleans first, then use validate_numbers which work with Number"""
        if isinstance(x2, bool):
            raise TypeError(f"Invalid {type(x2).__name__}, x2 must be a number, int or float")
        if isinstance(y2, bool):
            raise TypeError(f"Invalid {type(y2).__name__}, y2 must be a number, int or float")
        validate_number(x2)
        validate_number(y2)
        self.x = self.x + x2
        self.y = self.y + y2
        return self
        

    def _get_the_name(self) -> str:
        """Private helper, to return self.name or the type(self).__name__
        allows readable name for compare_with just below"""    
        if self.name:
            return self.name
        return type(self).__name__
        
    def compare_with(self, other: Any) -> str:
        """Public method, compare 2 shapes (or a number) and return a string.
        Shows:
        - same/different type
        - rounded area & perimeter for each
        - Encapsulation: uses private helpers _get_the_name and _area_of.
        
        Differences with __eq__ (comparing dimensions) include comparing, shapes, area, perimeter"""
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
    def __repr__(self) -> str: 
        return f"{type(self).__name__}(center x={self._x}, y={self._y})"

    # overriden in both children classes
    def __str__(self) -> str:
        raise NotImplementedError


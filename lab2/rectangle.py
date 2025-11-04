from shape import Shape
import math 
import matplotlib.pyplot as plt # maybe not needed her but rather in testing
from matplotlib.patches import Rectangle
# For the rectangle, I used https://www.youtube.com/watch?v=T8RXMRlRoRg


class Rectangle(Shape):
    #def __init__(self, x:int|float, y:int|float, length: int|float, width: int|float):
    def __init__(self, *args: int | float): #arg helps me if user forgets a value
        if len(args) != 4:
            raise ValueError(f"A missing value! Rectangle requires 4 values (x_value, y_value, length, width) got only {len(args)}/4!")
        
        x, y, length, width = args
        
        if not all(isinstance(v, (int, float)) for v in args):
            raise TypeError("All values must be int or float")
        
        super().__init__(x, y)
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if value is None:
            raise ValueError("Missing length value! You need to enter a length value")
        if not isinstance(value, (int, float)):
            raise TypeError(f"{value!r} is invalid. Length must be a positive number, integer or float, not {type(value).__name__}")
        if value <= 0:
            raise ValueError("Length must be a positive number greater than 0")
        self._length = value
        

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value is None:
            raise ValueError("Missing width value! You need to enter a width value")
        if not isinstance(value, (int, float)):
            raise TypeError(f"{value!r} is invalid. Width must be a positive number, integer or float, not {type(value):__name__}")
        if value <= 0:
            raise ValueError("Width must eb a proditve number greater than 0")
        self._width = value

#Overrides parent class
    @property
    def area(self):
        return self._length * self._width

#Overrides parent class
    @property
    def perimeter_is(self):
        return 2 * (self._length + self._width)

    #def is_square(self)-> bool:                ### easier but not great
    #    return self._length == self._width
    
    def is_square(self):                        ### better but no boolean, ??? a pb ???
        if self._length == self._width:
            return f"The shape is a square (all 4 sides = {self._length})"
        else:
            return f"Not a square (sides: length={self._length}, width={self._width})"
        
    def __repr__(self):
        return f"Rectangle(x={self.x}, y={self.y}, length={self._length}, width={self._width})"

    def __str__(self):
        return f"Point ({self.x}, {self.y}) is the center of the rectangle with length {self._length} and width {self._width}"

    def __eq__(self, other)-> bool:
        if not isinstance(other, Rectangle):
            return False
        # inclination is not a problem
        if self._length == other._length and self._width == other._width:
            return True
        if self._length == other._width and self._width == other._length:
            return True
        else:
            return False
        
    #def translate():
     

    # def draw(self): #?? do I need to pass here and write it in the test part??
    #     #fig, ax = plt.subplots()
    #     #bottom_left = (self.x - self._length / 2, self.y - self._width / 2)
    #     rect = Rectangle((self.x - self._length / 2, self.y - self._width / 2), self._length, self._width)
    #     ax.add_patch(rect)
    #     #ax.plot(self.x, self.y, 'ro')
    #     ax.set_xlim(-100, 100)
    #     ax.set_ylim(-100, 100)
    #     #ax.text(self.x, self.y, ' center', fontsize=8, ha='left', va='bottom')
    #     #ax.set_aspect('equal')
    #     #ax.grid(True, alpha=0.3)
    #     #plt.title(f"Rectangle: w={self._length}, h={self._width}, center=({self.x:.1f},{self.y:.1f})")
    #     #plt.show()

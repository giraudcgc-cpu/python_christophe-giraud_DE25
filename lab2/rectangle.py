
# For the rectangle, I used https://www.youtube.com/watch?v=T8RXMRlRoRg
from shape import Shape
import math
from utils import validate_positive, validate_number # !!! no import of _area_of here


class Rectangle(Shape):
    def __init__(self, x:int|float, y:int|float, length: int|float, width: int|float):     
        super().__init__(x, y)
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        validate_number(value)
        validate_positive(value, "length")
        self._length = value
        
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        validate_number(value)
        validate_positive(value, "width")
        self._width = value

#Overrides parent class
    @property
    def area(self):
        return self._length * self._width

#Overrides parent class
    @property
    def perimeter_is(self):
        return 2 * (self._length + self._width)
    
    def is_square(self):                        
        return self.length == self.width
                
    def __repr__(self):
        return f"{type(self).__name__}(x={self.x}, y={self.y}, length={self._length}, width={self._width}"

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
        return False
             

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

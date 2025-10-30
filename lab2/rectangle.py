from shape import Shapes
import math 
#from matplotlib.patches import Rectangle as rec
import matplotlib.pyplot as plt
import matplotlib.patches as patches
# For the rectangle, I used https://www.youtube.com/watch?v=T8RXMRlRoRg


class Rectangle(Shapes):
    def __init__(self, x:int|float =0, y:int|float =0, width: int|float = 3, height: int|float = 1):
        super().__init__(x, y)
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("width and height must be positive numbers, integer or float")
        if width <= 0 or height <= 0:
            raise ValueError("Enter a positive number greater than 0")
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

#overides
    @property
    def area(self):
        return self._width * self._height

#overides
    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    def is_square(self)-> bool:
        if self._width == self._height:
            return True 
        else:
            return False
    
    def __repr__(self):
        return f"Rectangle, center point @ (x={self.x}, y={self.y}, width={self._width}, height={self._height})"

    def __str__(self):
        return f"Point ({self.x}, {self.y}) is the center of the rectangle with width {self._width} and height {self._height}"

# as area and perimter are not enough, I keep it simple:
    def __eq__(self, other)-> bool:
        if not isinstance(other, Rectangle):
            return False
        if self._width == other._width and self._height == other._height:
            return True
        if self._width == other._height and self._height == other._width:
            return True
        else:
            return False
     

    def draw(self):
        fig, ax = plt.subplots(1)
    
        bottom_left = (self.x - self._width / 2, self.y - self._height / 2)
    
        rec = patches.Rectangle(bottom_left, self._width, self._height,
                          edgecolor='blue', linewidth=2)
        
        ax.add_patch(rec)
    
        ax.plot(self.x, self.y, 'ro')
        ax.text(self.x, self.y, ' center', fontsize=9, ha='left', va='bottom')
    
        ax.set_aspect('equal')
        ax.relim()
        ax.autoscale_view()
        ax.grid(True, alpha=0.3)
        plt.title(f"Rectangle: w={self._width}, h={self._height}, center=({self.x},{self.y})")
        plt.show()
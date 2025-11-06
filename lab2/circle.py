    
#error: did not know, had to import math, so math.pi was not defined
# import math found at https://www.w3schools.com/python/ref_math_pi.asp
# https://www.youtube.com/watch?v=T8RXMRlRoRg
# took pie from https://www.w3schools.com/python/ref_math_pi.asp

from shape import Shape
import math 
from utils import validate_number, validate_positive # !!! no import of _area_of here

class Circle(Shape):   
    def __init__(self, x:int|float, y:int|float,radius=1) -> None: 
        super().__init__(x, y)
        self.radius = radius      

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        validate_number(value)
        validate_positive(value, "radius")
        self._radius = value

#Overrides parent class
    @property
    def area(self):
        return math.pi * (self._radius ** 2)

#Overrides parent class
    @property
    def perimeter_is(self):
        return math.pi * self._radius * 2
    
    @property
    def perimeter_rounded(self):  
        return round(self.perimeter_is, 2)
              
    def unit_circle(self) -> bool:
        return self._radius == 1 and self._x == 0 and self._y == 0
# need to check test this with "x" 

#Overrides if same radius, they have same area and same perimeter. ignoring center postion
    def __eq__(self, other) -> bool:
        if not isinstance(other, Circle):
            return False
        # To be equal, same center and radius
        return self._radius == other._radius    
    
#Overrides
    def __repr__(self):
        return f"{type(self).__name__}(x={self._x}, y={self._y}, radius={self._radius})"

#Overrides
    def __str__(self):
        return f"This circle has center coordinates x={self._x}, y={self._y} and a radius of {self._radius}"


#Overrides
# matplotlib https://www.geeksforgeeks.org/python/how-to-draw-a-circle-using-matplotlib-in-python/
#def draw(self):
  #  fig, ax = plt.subplots()
# Circle(xy, radius, color, ...)
   # circle = plt.Circle((self.x, self.y), radius, color='red', fill=False)
# Add the circle to the axes
   # ax.add_patch(circle)
# Ensure the circle is not distorted (x and y axes have the same scale)
   # ax.set_aspect('equal', adjustable='box')
# Display
   # plt.show()
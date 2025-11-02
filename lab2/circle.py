from shape import Shape
import matplotlib.pyplot as plt # maybe not needed her but rather in testing
import math     #error: did not know, had to import math, so math.pi was not defined
# import math found at https://www.w3schools.com/python/ref_math_pi.asp
# https://www.youtube.com/watch?v=T8RXMRlRoRg
# took pie from https://www.w3schools.com/python/ref_math_pi.asp

class Circle(Shape):   #inheritance
    def __init__(self, x:int|float, y:int|float, radius) -> None: #radius must be minimum 1, "by default"
        super().__init__(x, y)
        self.radius = radius      

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Radius must be a number, integer or float")
        if value <= 0:
            raise ValueError(f"Radius must be a positive number as distance is positive")
        self._radius = value

#Overrides parent class
    @property
    def area(self):
        return math.pi * (self._radius ** 2)

#Overrides parent class
    @property
    def perimeter(self):
        return math.pi * self._radius * 2
              
    def is_a_unit_circle(self) -> bool:
        if self._radius == 1 and self._x == 0 and self._y == 0:
            return True
        else:
            return False

#overides
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        if self._radius == other._radius:   # error: had 0 instead of ==
            return True
    
#overides
    def __repr__(self):
        return f"Circle, radius= {self._radius}, center at x={self._x}, y={self._y}"

#overides
    def __str__(self):
        return f"This circle has center coordinates x={self._x}, y={self._y} and a radius of {self._radius}"

#overides
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
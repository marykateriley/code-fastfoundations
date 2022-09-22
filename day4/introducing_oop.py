import sys
import math
import os
import turtle


class Circle:
    units = 'cm'  # all circles will have the same units
    units_squared = 'cm' '\u00B2'  # this is the hexadecimal to square the unit defined

    def __init__(self, radius, position=(0, 0), fill="white", stroke="black"):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.diameter = radius * 2
        self.fill = fill
        self.stroke = stroke
        # self.area = math.pi * radius**2 # have commented this out as we went on to define area below

    def __str__(self):  # Python special methods
        return f"I am a circle of size radius = {self.radius} {self.units}, diameter = {self.diameter} {self.units}, located at {self.position}."

    # referencing the radius and units located at position

    def area(self):
        return f"Area = {math.pi * self.radius ** 2}"

    def perimenter(self):
        return f"Perimeter = {2 * math.pi * self.radius ** 2}"

    def arc_length(self, angle, degrees=False):  # have to make this true when running the function to get degrees
        """Function to compute the arc length l for the angle provided"""
        if degrees:
            angle = math.radians(angle)
        return f"Arc Length = {self.radius * angle}"

    def bounding_box(self):
        """Function to compute the four values of the bounding box for a circle"""
        xmin = self.position[0] - self.radius,
        xmax = self.position[0] + self.radius,
        ymin = self.position[1] - self.radius,
        ymax = self.position[1] + self.radius
        return f"Bounding Box = {xmin, xmax, ymin, ymax}"


class Rectangle:
    def __init__(self, width, height, position=(0, 0), fill="white", stroke="black", angle=0.0):
        self.width = width
        self.height = height
        self.position = position
        self.fill = fill
        self.stroke = stroke
        self.angle = angle

    def area(self):
        return f"Area = {self.width * self.height}"

    def perimeter(self):
        return f"Perimeter = {(self.width * 2) + (self.height * 2)}"

    def diagonal(self):
        return f"Diagonal = {math.sqrt(self.width ** 2 + self.height ** 2)}"

    def bounding_box(self):
        xmin = self.position[0] - 0.5 * self.width,  # or can do self.width / 2
        xmax = self.position[0] + 0.5 * self.width,
        ymin = self.position[1] - 0.5 * self.height,
        ymax = self.position[1] + 0.5 * self.height,
        return f"Bounding Box = {xmin, xmax, ymin, ymax}"


class Square(Rectangle):  # inherited from parent class, rectangle
    def __init__(self, width, *args, **kwargs):
        super().__init__(width, width, *args, **kwargs)  # super() for super/parent classes


class Canvas(turtle.TurtleScreen):
    def __init__(self, width, height, bg="white"):
        canvas = turtle.getcanvas()
        super().__init__(canvas) # canvas has now became a turtle.TurtleScreen object
        self.screensize(width, height, bg=bg)
        self.width = width
        self.height = height
    def __str__(self):
        return f"Canvas of dimensions = ({self.width}, {self.height})"


class Text:
    def __int__(self, text, position=(0, 0), colour="black"):
        self.text = text
        self.position = position
        self.colour = colour


def main():
    small_circle = Circle(10)
    big_circle = Circle(50)
    print(small_circle.area())  # this needs a specifc circle defined, not a number
    print(small_circle.perimenter())
    print(small_circle.arc_length(100, True))
    print(small_circle.bounding_box())

    my_rectangle = Rectangle(4, 5, (0, 0), )
    print(my_rectangle.area())
    print(my_rectangle.perimeter())
    print(my_rectangle.diagonal())
    print(my_rectangle.bounding_box())

    my_square = Square(4)
    print(my_square.area())
    print(my_square.perimeter())
    print(my_square.diagonal())
    print(my_square.bounding_box())

    my_canvas = Canvas(1200, 750)
    print(my_canvas)
    turtle.done()


if __name__ == "__main__":
    sys.exit(main())

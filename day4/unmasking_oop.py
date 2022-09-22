import math
import os
import sys


class Circle:
    units = 'cm'  # all circles will have the same units
    units_squared = 'cm' '\u00B2' # this is the hexadecimal to square the unit defined

    def __init__(self, radius, position=(0, 0), fill = "white", stroke = "black"):
        self.radius = radius  # each circle will have a particular radius
        self.position = position
        self.diameter = radius * 2
        self.fill = fill
        self.stroke = stroke
        #self.area = math.pi * radius**2 # have commented this out as we went on to define area below

    def __str__(self):  # Python special methods
        return f"I am a circle of size radius = {self.radius} {self.units}, diameter = {self.diameter} {self.units}, located at {self.position}."
    # referencing the radius and units located at position


    def area(self):
        return f"Area = {math.pi * self.radius ** 2}"


    def perimenter(self):
        return f"Perimeter = {2 * math.pi * self.radius ** 2}"


    def arc_length(self, angle, degrees=False): # have to make this true when running the function to get degrees
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



def main():
    small_circle = Circle(10)
    big_circle = Circle(50)

    print(small_circle)
    print(big_circle)

    # now we change units for all instances on the class
    Circle.units = 'pm'

    print(small_circle)
    print(big_circle)

    # but
    big_circle.units = 'hm'  # only change for the big_circle instance

    print(small_circle)
    print(big_circle)

    #canvas = Canvas(1200, 780)
   # canvas.mystery_method()
    #turtle.done()

#TASK
    print(small_circle.area()) # this needs a specifc circle defined, not a number
    print(small_circle.perimenter())
    print(small_circle.arc_length(100, True))
    print(small_circle.bounding_box())

    return os.EX_OK


if __name__ == '__main__':
    sys.exit(main())

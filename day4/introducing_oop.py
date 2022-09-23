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
    def draw(self, pen):
        if pen.isdown():
            pen.up()
        pen.goto(*self.position) # enables it to be drawn at any position
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.circle(self.radius)
        pen.end_fill()
        pen.up()




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

    def draw(self, pen): # writing how to draw a rectangle in this code block
        if pen.isdown():
            pen.up()
        pen.goto(*self.position) # enables rectangle to be drawn at any position
        pen.down()
        pen.begin_fill()
        pen.pencolor(self.stroke)
        pen.fillcolor(self.fill)
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.right(90)
        pen.forward(self.width)
        pen.right(90)
        pen.forward(self.height)
        pen.right(90)
        pen.end_fill()
        pen.up()





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
        self.pen = turtle.RawTurtle(canvas)


    def draw_axis(self):
        self.pen.up()
        self.pen.goto(0, self.height / 2)
        self.pen.down()
        self.pen.goto(0, -self.height / 2)
        self.pen.up()
        self.pen.goto(-self.width / 2, 0)
        self.pen.down()
        self.pen.goto(self.width / 2, 0)
        self.pen.up()
        self.pen.home()

    def __str__(self):
        return f"Canvas of dimensions = ({self.width}, {self.height})"

    def draw_circle(self, circle):
        self.pen.circle(circle.radius) # taking the circle class previously created e.g. small_circle

    def draw(self, shape):
        shape.draw(self.pen)

    def write(self, text):
        text.write(self.pen)

class Text: ## CHECK SOLUTION
    def __init__(self, text, position=(0, 0), colour='black', move=False, align='left', font=('Arial', 8, 'normal')):
        self.text = text
        self.position = position
        self.colour = colour
        self.move = move
        self.align = align
        self.font = font

    def write(self, pen):
        if pen.isdown():
            pen.up()
        pen.goto(*self.position)
        pen.write(self.text, move=self.move, align=self.align, font=self.font)
        pen.up()

    def __str__(self):
        return self.text


def main():
    small_circle = Circle(10)
    big_circle = Circle(100, position=(20, -10), fill="red", stroke="yellow")
    print(small_circle.area())  # this needs a specifc circle defined, not a number
    print(small_circle.perimenter())
    print(small_circle.arc_length(100, True))
    print(small_circle.bounding_box())

    my_rectangle = Rectangle(30, 50, position=(100, -15), fill='grey', stroke='indigo')
    print(my_rectangle.area())
    print(my_rectangle.perimeter())
    print(my_rectangle.diagonal())
    print(my_rectangle.bounding_box())

    my_square = Square(30)
    print(my_square.area())
    print(my_square.perimeter())
    print(my_square.diagonal())
    print(my_square.bounding_box())

    my_canvas = Canvas(1200, 750)
    print(my_canvas)
    #my_canvas.draw_axis()
    #my_canvas.draw_circle(small_circle)
    #my_canvas.draw(small_circle)
    #my_canvas.draw(big_circle)
    #my_canvas.draw(my_rectangle)
    #my_canvas.draw(my_square)
    text = Text("this is cool!", font=('Helvetica', 20, 'bold'), position=(-100, -100))
    my_canvas.write(text)
    turtle.done()


if __name__ == "__main__":
    sys.exit(main())

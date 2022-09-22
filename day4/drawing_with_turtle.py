import sys
import turtle


def draw_rectangle():
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)


def draw_circle():
    pen = turtle.Turtle() # the turtle is the pen
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(60)
    pen.end_fill()
    pen.up()

#TASK
def draw_triangle(): #equilateral triangle
    pen = turtle.Turtle()
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.left(120)
    pen.forward(100)
    pen.begin_fill()
    pen.fillcolor("green")
    pen.pencolor("purple")
    pen.end_fill()

def draw_pentagon(): # upside down due to 288 angle
    pen = turtle.Turtle()
    pen.forward(150)
    pen.left(288)
    pen.forward(150)
    pen.left(288)
    pen.forward(150)
    pen.left(288)
    pen.forward(150)
    pen.left(288)
    pen.forward(150)

def draw_pentagon2(): # right way up due to 72 angle
    pen = turtle.Turtle()
    pen.forward(150)
    pen.left(72)
    pen.forward(150)
    pen.left(72)
    pen.forward(150)
    pen.left(72)
    pen.forward(150)
    pen.left(72)
    pen.forward(150)

def draw_polygon(n, length=10, position=(0,0), fill="white", stroke="black"):
    n = (n-2) * 180
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(*position)
    pen.down()






def main():
    #draw_rectangle()
    #draw_circle()
    #draw_triangle()
    draw_pentagon()
    #draw_pentagon2()
    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())

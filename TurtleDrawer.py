from TIGr import AbstractDrawer
import turtle
from ErrorChecking import ErrorChecking as EC


class TurtleDrawer(AbstractDrawer):
    def __init__(self):
        self.penlist = ["", "white", "black", "red", "yellow", "blue"]
        self.turtle = turtle.Turtle()
        self.pen_up()
        self.check = EC().check  # error checking class

    def select_pen(self, pen_num):
        if int(pen_num) > 5 or int(pen_num) < 1:
            print("Only use pens 1-5")
        else:
            self.turtle.pencolor(self.penlist[int(pen_num)])

    def pen_down(self):
        self.turtle.pendown()

    def pen_up(self):
        self.turtle.penup()

    def go_along(self, along):
        self.check(along, "int", "along, go_along, TurtleDrawer()")
        currentX = self.turtle.xcor()
        if self.turtle.isdown():
            self.turtle.penup()
            self.turtle.setx(currentX + int(along))
            self.turtle.pendown()
        else:
            self.turtle.setx(currentX + int(along))

    def go_down(self, down):
        self.check(down, "int", "down, go_down, TurtleDrawer()")
        currentY = self.turtle.ycor()
        if self.turtle.isdown():
            self.turtle.penup()
            self.turtle.sety(currentY + int(down))
            self.turtle.pendown()
        else:
            self.turtle.sety(currentY + int(down))

    def draw_line(self, direction, distance):
        direction = int(direction)
        distance = int(distance)
        self.check(direction, "floatOrInt", "direction, draw_line, TurtleDrawer()")
        self.check(distance, "floatOrInt", "distance, draw_line, TurtleDrawer()")
        if direction == 90 or direction == 270:
            direction -= 90
        else:
            direction += 90
        self.turtle.seth(direction)
        if self.turtle.isdown():
            self.turtle.forward(distance)

    def draw_circle(self, size):
        size = int(size)
        self.check(size, "floatOrInt", "size, draw_circle, TurtleDrawer()")
        self.turtle.circle(size)

    def draw_rectangle(self, size):
        self.check(size, "int", "size, draw_rectangle, TurtleDrawer()")
        ourDirection = 0
        for i in range(4):
            self.draw_line(ourDirection, size)
            ourDirection += 90

    def draw_triangle(self, size):
        size = int(size)
        self.check(size, "floatOrInt", "size, draw_triangle, TurtleDrawer()")
        self.turtle.seth(0)
        for i in range(3):
            self.turtle.left(120)
            self.turtle.forward(1 * size)

    def end(self):
        self.turtle.getscreen()._root.mainloop()

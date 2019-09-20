import tkinter
from TIGr import AbstractDrawer
from Dest import *


class TkinterDrawer(AbstractDrawer):
    def __init__(self):
        self.top = tkinter.Tk()
        self.myCanvas = tkinter.Canvas(self.top, bg="grey", height=500, width=500)
        self.color = "white"
        self.penDown = False
        self.x = 250
        self.y = 250
        self.myDest = Dest()
        self.penlist = ["", "white", "black", "red", "yellow", "blue"]
        self.check = Ec().check  # error checking class

    def select_pen(self, pen_num):
        if int(pen_num) > 5 or int(pen_num) < 1:
            print("Only use pens 1-5")
        else:
            self.color = self.penlist[int(pen_num)]

    def pen_down(self):
        self.penDown = True

    def pen_up(self):
        self.penDown = False

    def go_along(self, along):
        self.check(along, "floatOrInt", "along, go_along, TkinterDrawer()")
        self.x = along

    def go_down(self, down):
        self.check(down, "floatOrInt", "down, go_down, TkinterDrawer()")
        self.y = down

    def draw_line(self, direction, distance):
        if direction == 0:
            direction = 180
        elif direction == 180:
            direction = 0
        self.check(direction, "int", "direction, draw_line, TkinterDrawer()")
        self.check(distance, "int", "distance, draw_line, TkinterDrawer()")
        my_position = [self.x, self.y]
        distance = int(distance)
        new_coords = self.myDest.getdestination(my_position, direction, distance)
        if self.penDown:
            self.myCanvas.create_line(self.x, self.y, new_coords[0], new_coords[1], fill=self.color)
        self.go_along(new_coords[0])
        self.go_down(new_coords[1])
        self.x = new_coords[0]
        self.y = new_coords[1]

    def draw_circle(self, radius):
        self.check(radius, "int", "radius, draw_circle, TkinterDrawer()")
        x = self.x
        y = self.y
        x0 = x - radius
        y0 = y - radius
        x1 = x + radius
        y1 = y + radius
        self.myCanvas.create_oval(x0, y0, x1, y1)

    def draw_rectangle(self, size):
        self.check(size, "int", "size, draw_rectangle, TkinterDrawer()")
        self.go_along(250)
        self.go_down(250)
        array_dir = (0, 90, 180, 270)
        for i in range(4):
            self.draw_line(array_dir[i - 1], size)

    def draw_triangle(self, size):
        self.myCanvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

    def end(self):
        self.myCanvas.pack()
        self.top.mainloop()

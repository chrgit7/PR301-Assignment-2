import tkinter
from TIGr import AbstractDrawer
from Dest import *
from TkinterDrawerExtend import TkinterDrawerExtend as TKExtend


class TkinterDrawer(AbstractDrawer, TKExtend):
    def __init__(self):
        super().__init__(self)
        self.top = tkinter.Tk()
        self.myCanvas = tkinter.Canvas(self.top, bg="grey", height=500,
                                       width=500)
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
        TKExtend.draw_line(self, direction, distance)

    def draw_circle(self, radius):
        TKExtend.draw_circle(self, radius)

    def draw_rectangle(self, size):
        TKExtend.draw_rectangle(self, size)

    def draw_triangle(self, size):
        TKExtend.draw_triangle(self, size)

    def end(self):
        TKExtend.end(self)

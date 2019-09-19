import turtle
from cmd import Cmd
from TurtleDrawer import *


class TurtlePrompt(TurtleDrawer, Cmd):
    def __init__(self):
        super().__init__()
        Cmd.__init__(self)
        self.alias = {
            'P': self.do_p,
            'D': self.do_d,
            'U': self.do_u,
            'X': self.do_x,
            'Y': self.do_y,
            'N': self.do_n,
            'S': self.do_s,
            'E': self.do_e,
            'W': self.do_w
        }

    def do_p(self, arg):
        """Select Pen (1-5)"""
        super().select_pen(arg)

    def do_d(self, arg):
        """Pen Down"""
        super().pen_down()

    def do_u(self):
        """Pen Up"""
        super().pen_up()

    def do_x(self, arg):
        """Go along (x coordinate)"""
        super().go_along(arg)

    def do_y(self, arg):
        """Go down(y coordinate)"""
        super().go_down(arg)

    def do_n(self, arg):
        """Go North"""
        print(arg)
        super().draw_line(0, arg)

    def do_e(self, arg):
        """Go East"""
        print(arg)
        super().draw_line(90, arg)

    def do_w(self, arg):
        """Go West"""
        print(arg)
        super().draw_line(270, arg)

    def do_s(self, arg):
        """Go South"""
        print(arg)
        super().draw_line(180, arg)

    def do_c(self, arg):
        """Draw Cricle"""
        print(arg)
        super().draw_circle(arg)

    def do_r(self, arg):
        """Draw Rectangle"""
        print(arg)
        super().draw_rectangle(arg)

    def do_t(self, arg):
        """Draw Triangle"""
        print(arg)
        super().draw_triangle(arg)

    def do_exit(self, arg):
        """Exit Turtle"""
        return True

    def default(self, line):
        cmd, arg, line = self.parseline(line)
        if cmd in self.alias:
            self.alias[cmd](arg)
        else:
            print("** Unknown syntax")

    def go(self):
        TurtlePrompt.cmdloop(self)

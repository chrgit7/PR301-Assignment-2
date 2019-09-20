from TIGr import AbstractParser


class MyParser(AbstractParser):
    def __init__(self, drawer):
        super().__init__(drawer)
        self.draw_command = {
            'D': lambda: self.drawer.pen_down(),
            'P': lambda: self.drawer.select_pen(self.data),
            'N': lambda: self.drawer.draw_line(0, self.data),
            'E': lambda: self.drawer.draw_line(90, self.data),
            'S': lambda: self.drawer.draw_line(180, self.data),
            'W': lambda: self.drawer.draw_line(270, self.data),
            'X': lambda: self.drawer.go_along(self.data),
            'Y': lambda: self.drawer.go_down(self.data),
            'U': lambda: self.drawer.pen_up(),
            'C': lambda: self.drawer.draw_circle(self.data),
            'R': lambda: self.drawer.draw_rectangle(self.data),
            'T': lambda: self.drawer.draw_triangle(self.data)
        }

    def parse(self, raw_source):
        self.source = raw_source

        for line in self.source:
            temp_arr = line.split(" ")
            self.command = line[0]
            try:
                self.data = int(temp_arr[1])
            except IndexError:
                self.data = 0
            self.draw_command[self.command]()
        try:
            self.drawer.end()
        except NameError:
            pass

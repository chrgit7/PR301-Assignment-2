from TIGr import AbstractParser


class MyParser(AbstractParser):
    def __init__(self, drawer):
        super().__init__(drawer)

    def parse(self, raw_source):
        self.source = raw_source

        for line in self.source:
            tempArr = line.split(" ")
            self.command = line[0]
            try:
                self.data = int(tempArr[1])
            except:
                self.data = 0
            if self.command == 'D':
                self.drawer.pen_down()
            if self.command == 'P':
                self.drawer.select_pen(self.data)
            if self.command == 'N':
                self.drawer.draw_line(0, self.data)
            if self.command == 'E':
                self.drawer.draw_line(90, self.data)
            if self.command == 'S':
                self.drawer.draw_line(180, self.data)
            if self.command == 'W':
                self.drawer.draw_line(270, self.data)
            if self.command == 'D':
                self.drawer.pen_down()
            if self.command == 'P':
                self.drawer.select_pen(self.data)
            if self.command == 'X':
                self.drawer.go_along(self.data)
            if self.command == 'Y':
                self.drawer.go_down(self.data)
            if self.command == 'U':
                self.drawer.pen_up()
            if self.command == 'C':
                self.drawer.draw_circle(self.data)
            if self.command == 'R':
                self.drawer.draw_rectangle(self.data)
            if self.command == 'T':
                self.drawer.draw_triangle(self.data)
        try:
            self.drawer.end()
        except:
            pass

class TkinterDrawerExtend:
    def __init__(self, sub_class):
        self.sc = sub_class

    def draw_line(self, direction, distance):
        if direction == 0:
            direction = 180
        elif direction == 180:
            direction = 0
        self.sc.check(direction, "int", "direction, draw_line,"
                                        "TkinterDrawerExtend()")
        self.sc.check(distance, "int", "distance, draw_line,"
                                       "TkinterDrawerExtend()")
        my_position = [self.sc.x, self.sc.y]
        distance = int(distance)
        new_coords = self.sc.myDest.getdestination(my_position, direction,
                                                   distance)
        if self.sc.penDown:
            self.sc.myCanvas.create_line(self.sc.x, self.sc.y,
                                         new_coords[0], new_coords[1],
                                         fill=self.sc.color)
        self.sc.go_along(new_coords[0])
        self.sc.go_down(new_coords[1])
        self.sc.x = new_coords[0]
        self.sc.y = new_coords[1]

    def draw_circle(self, radius):
        self.sc.check(radius, "int", "radius, draw_circle, TkinterDrawer()")
        x = self.sc.x
        y = self.sc.y
        x0 = x - radius
        y0 = y - radius
        x1 = x + radius
        y1 = y + radius
        self.sc.myCanvas.create_oval(x0, y0, x1, y1)

    def draw_rectangle(self, size):
        self.sc.check(size, "int", "size, draw_rectangle, TkinterDrawer()")
        self.sc.go_along(250)
        self.sc.go_down(250)
        array_dir = (0, 90, 180, 270)
        for i in range(4):
            self.sc.draw_line(array_dir[i - 1], size)

    def draw_triangle(self, size):
        self.sc.myCanvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)

    def end(self):
        self.sc.myCanvas.pack()
        self.sc.top.mainloop()

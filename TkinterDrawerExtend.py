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

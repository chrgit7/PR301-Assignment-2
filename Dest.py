import math
from ErrorChecking import ErrorChecking as Ec


# Not my code
class Dest:  # returns the destination x,y coordinates given a current position, direction and distance
    def getdestination(self, currentpos, direction, distance):
        Ec().check(direction, "int", "direction, getDestination, Dest()")  # checking if arguments are of correct type
        Ec().check(distance, "int", "distance, getDestination, Dest()")
        Ec().check(currentpos, "list", "currentPos, getDestination, Dest()")
        direction = float(direction)
        # Compute the change in position
        delta_y = distance * math.cos(math.radians(direction))
        delta_x = distance * math.sin(math.radians(direction))
        # Add that to the existing position
        new_x = currentpos[0] + delta_x
        new_y = currentpos[1] + delta_y
        return new_x, new_y

from compassDirections import compassDirections

class RobotPosition(object):

    def __init__(self):
        self.x =0
        self.y = 0
        self.z = 0.00
        self.direction = compassDirections.north
        self.currentNode = 'n1'


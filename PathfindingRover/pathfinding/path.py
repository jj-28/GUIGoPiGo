from PathfindingRover.pathfinding.compassDirections import compassDirections

class path(object):
    """description of class"""

    def __init__(self):
        self.nodes = [] # the nodes list of a path
        self.commands = [] # string list of commands for robot controller


    #get a path of strings for the robot to use
    def getPathAsStrings(self,robotpos):
        i = 0 #the node index
        j = 0 #directions index
        fakepos = robotpos
        fakepos.direction = robotpos.direction

        #while we have nodes to process
        while(len(self.nodes) -1 > i):
            #get the next node
            node = self.nodes[i]
            #if not the first node
            if not i == 0:
                #set robot direction opposite to direction it came
                edge = self.nodes[i-1].getEdge(self.nodes[i])
                tempDirection =  edge.getDirection(self.nodes[i])
                fakepos.direction = self.reverseDirection(tempDirection)
            #get the edge we need
            edge = self.nodes[i].getEdge(self.nodes[i+1])
            direction = edge.getDirection(node)
            #while we aren't facint the correct direction
            if(fakepos.direction != direction ):
                self.commands.append(self.getDirection(direction,fakepos.direction))
                j = j+1
            self.commands.append("Forward")
            #prep for next node
            i = i +1
            j = j+1

        return self.commands

    def reverseDirection(self,d):
        if(d == compassDirections.north):
            return compassDirections.south
        elif(d == compassDirections.east):
            return compassDirections.west
        elif(d == compassDirections.west):
            return compassDirections.east
        elif(d == compassDirections.south):
            return compassDirections.north

    def getDirection(self,d1,d2):

        if(d1 == compassDirections.north):
            if(d2 == compassDirections.west):
                return "Right"
            elif(d2 == compassDirections.east):
                return "Left"
            elif(d2 == compassDirections.south):
                return "TurnAround"
        elif(d1 == compassDirections.east):
            if(d2 == compassDirections.north):
                return "Right"
            elif(d2 == compassDirections.south):
                return "Left"
            elif(d2 == compassDirections.west):
                return "TurnAround"
        elif(d1 == compassDirections.south):
            if(d2 == compassDirections.east):
                return "Right"
            elif(d2 == compassDirections.west):
                return "Left"
            elif(d2 == compassDirections.north):
                return "TurnAround"
        elif(d1 == compassDirections.west):
            if(d2 == compassDirections.south):
                return "Right"
            elif(d2 == compassDirections.north):
                return "Left"
            elif(d2 == compassDirections.east):
                return "TurnAround"
            
            





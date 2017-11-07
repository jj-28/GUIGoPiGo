
class Node(object):
    """description of class
    This class will point to other nodes for pathfinding and will use directions.
    """
    
    def __init__(self, inName,x,y):
        self.name = inName
        self.gCost
        self.hCost
        self.x = x
        self.y = y
        self.northEdge  # the north edge
        self.eastEdge  # the east edge
        self.southEdge  # the south edge
        self.westEdge  # the south edge
        self.parent = None
        self.edges = [self.northEdge, self.eastEdge, self.southEdge, self.westEdge]
    def putEdgesOnArray(self):
        self.edges = [self.northEdge,self.eastEdge,self.southEdge,self.westEdge]

    def getEdge(self,otherNode):
        for currentEdge in self.edges:
            if(currentEdge.getOtherNode(self) == otherNode ):
                return currentEdge
        return None

    def fCost(self):
        return self.gCost + self.hCost

    def __le__(self, other):
        return self.fCost() <= other.fCost

    def __lt__(self, other):
        return self.fCost() <= other.fCost

    def __gt__(self, other):
        return self.fCost() > other.fCost

    def __ge__(self, other):
        return self.fCost() >= other.fCost

    def __eq__(self, other):
        return self.fCost() == other.fCost




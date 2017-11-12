from compassDirections import compassDirections

class Node(object):
    """description of class
    This class will point to other nodes for pathfinding and will use directions.
    """
    def __init__(self):
        self.name = ''
        self.gCost = 0
        self.hCost = 0
        self.x = 0
        self.y = 0
        self.northEdge = edge() # the north edge
        self.eastEdge = edge() # the east edge
        self.southEdge = edge() # the south edge
        self.westEdge = edge() # the south edge
        self.parent = None
        self.edges = [self.northEdge, self.eastEdge, self.southEdge, self.westEdge]

    def __init__(self, inName,x,y):
        self.name = inName
        self.gCost = 0
        self.hCost = 0
        self.x = x
        self.y = y
        self.northEdge = ''#edge(None,None,None,None,0,False) # the north edge
        self.eastEdge = ''#edge() # the east edge
        self.southEdge = ''#edge() # the south edge
        self.westEdge = ''#edge() # the south edge
        self.parent = None
        self.edges = [self.northEdge, self.eastEdge, self.southEdge, self.westEdge]
    def putEdgesOnArray(self):
        self.edges = [self.northEdge,self.eastEdge,self.southEdge,self.westEdge]

    def getEdge(self,otherNode):
        for currentEdge in self.edges:
            if type(currentEdge) is edge:
                if(currentEdge.getOtherNode(self) == otherNode ):
                    return currentEdge
        return None

    def fCost(self):
        return self.gCost + self.hCost

    def __le__(self, other):
        return self.hCost <= other.hCost

    def __lt__(self, other):
        return self.hCost <= other.hCost

    def __gt__(self, other):
        return self.hCost > other.hCost

    def __ge__(self, other):
        return self.hCost >= other.hCost

    def __eq__(self, other):
        return self.name == other.name

class edge(object):
    """description of class
    this class contains info about an edge between two nodes
    """
    def __init__(self):
        self.n1 = Node()
        self.d1 = compassDirections.north
        self.n2 = Node()
        self.d2 = compassDirections.north
        self.weight = 0
        self.inObstacle = False
    def __init__(self,inNode1,inDirection1,inNode2,inDirection2,inWeight,inObstacle):
        self.n1 = inNode1               #the first node
        self.d1 = inDirection1          #direction this edge comes from the first node
        self.n2 = inNode2               #the 2nd node
        self.d2 = inDirection2          #direction this edge comes from the second node
        self.weight = inWeight          #the distance between these two nodes
        self.inObstacle = inObstacle    #is there an obstacle?

        self.__assign(self.n1,self.d1)
        self.__assign(self.n2,self.d2)

    def __assign(self,n,d):
        if d == compassDirections.north :
            n.northEdge = self
        elif d == compassDirections.east:
            n.eastEdge = self
        elif d == compassDirections.south:
            n.southEdge = self
        elif d == compassDirections.west:
            n.westEdge = self
        n.putEdgesOnArray()

    def getOtherNode(self,node):
        if node == self.n1:
            return self.n2
        elif node == self.n2:
            return self.n1
        else:
            return None

    def getDirection(self,node):
        if self.n1 == node:
            return self.d1
        elif self.n2 == node:
            return self.d2
        else:
            return None

    def isStraightEdge(self):
        if(self.d1 + self.d2)%2 ==0:
            return True
        else:
            return False



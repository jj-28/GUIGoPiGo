import compassDirections
class edge(object):
    """description of class
    this class contains info about an edge between two nodes
    """

    def __init__(self,inNode1,inDirection1,inNode2,inDirection2,inWeight,inObstacle):
        self.n1 = inNode1               #the first node
        self.d1 = inDirection1          #direction this edge comes from the first node
        self.n2 = inNode2               #the 2nd node
        self.d2 = inDirection2          #direction this edge comes from the second node
        self.weight = inWeight          #the distance between these two nodes
        self.inObstacle = inObstacle    #is there an obstacle?

        self.__assign(self,self.n1,self.d1)
        self.__assign(self,self.n2,self.d2)

    def __assign(self,n,d):
        if d == compassDirections.north :
            n.northEdge = self
        elif d == compassDirections.east:
            n.eastEdge = self
        elif d == compassDirections.south:
            n.southEdge = self
        elif d == compassDirections.west:
            n.southEdge = self

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



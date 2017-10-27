import edge

class Node(object):
    """description of class
    This class will point to other nodes for pathfinding and will use directions.
    """

    northEdge #the edge facing north, 
    eastEdge #the east edge
    southEdge #the south edge
    westEdge #the south edge
    edges[] = {northEdge,eastEdge,southEdge,westEdge}
    
    def getEdge(otherNode)
        for currentEdge in edges
            if(currentEdge.getOtherNode(self) = otherNode )
                return currentEdge
        return None




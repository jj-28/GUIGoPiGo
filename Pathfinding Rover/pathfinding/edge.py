import Node
import compassDirections

class edge(object):
    """description of class
    this class contains info about an edge between two nodes
    """
    n1  #the first node
    d1  #direction this edge comes from the first node
    n2  #the 2nd node
    d2  #direction this edge comes from the second node
    weight #the distance between these two nodes
    obstacle #is there an obstacle?

    def __init__(inNode1,inDirection1,inNode2,inDirection2,inWeight,inObstacle)
        n1 = inNode1
        d1 = inDirection1
        n2 = inNode2
        d2 = inDirection2
        weight = inWeight
        inObstacle = inObstacle

    def getOtherNode(node)
        if(node = n1)
            return n2
        else if(node = n2)
            return n1
        else
            return None

    def getDirection(node)
        if n1 = node
            return d1
        else if n2 = node
            return d2
        else 
            return None



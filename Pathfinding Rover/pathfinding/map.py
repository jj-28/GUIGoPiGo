import mapAssembler
import math
from priodict import priorityDictionary
class map(object):
    """description of class
    this class is responsible returning paths from a map
    """


    def __init__(self):
        self.nodes = mapAssembler.assembleMap() #nodes of the map
    def getPath(self,start,end):
        path = self.__pathfinding(start,end)
        return path

    #A* pathfinding solution
    #TODO determine how to allow for weights
    def __pathfinding(self,start,end):
        # initialize components
        pathSuccess = False
        openSet = []
        closedSet = []
        neighborList = []
        currentNode = None
        newMovementCost = 0
        path = 0

        openSet.__add__(start)
        while(openSet.count >0 and currentNode != end):
            currentNode = openSet.pop()
            closedSet.__add__(currentNode)

            if(currentNode == end):
                pathSuccess = True

            neighborList.clear()
            neighborList = currentNode.edges
            for neighbor in neighborList:
                if(not closedSet.__contains__(neighbor)):
                    newMovementCost = currentNode.gCost + currentNode.getDirection().weight
                    if(newMovementCost < neighbor.gCost or not openSet.__contains__(neighbor)):
                        neighbor.gCost = newMovementCost
                        neighbor.hCost = self.getDistance(neighbor,end)
                        neighbor.parent = currentNode

                        if(not openSet.__contains__(neighbor)):
                            openSet.__add__(neighbor)
                        #else:
                            #openSet.updateitem neighbor


        if pathSuccess:
            waypoints = self.tracePath(start,end)
            return waypoints
        else:
            return None

    def tracePath(self,start,end):
        path = []
        currentNode = end

        while currentNode != start:
            path.__add__(currentNode)
            currentNode = currentNode.parent
        path.add(start)
        path.reverse()
        return path

    def getDistance(self,a,b):
        x = math.fabs(a.x - b.x)
        y = math.fabs(a.y - a.y)
        return x+y
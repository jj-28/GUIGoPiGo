from mapAssembler import mapAssembler
from Node import Node
from Node import edge
from path import path
import math
import sys


# from priodict import priorityDictionary
class map(object):
    """description of class
    this class is responsible returning paths from a map
    """

    def __init__(self):
        mapper = mapAssembler()
        self.nodes = []
        self.nodes = mapper.assembleMap()  # nodes of the map

    def findNode(self,name):
        for node in self.nodes:
            if(node.name == name):
                return node
        return None

    def getPath(self, start, end):
        mypath = path()
        mypath.nodes = self.__pathfinding(start, end)
        return mypath

    # A* pathfinding solution
    # TODO determine how to allow for weights
    def __pathfinding(self, start, end):
        # initialize components
        pathSuccess = False
        openSet = []
        closedSet = []
        neighborList = []
        currentNode = Node('',0,0)
        newMovementCost = 0
        path = 0
        count = 0
        openSet.append(start)
        count = openSet.__len__()
        while (len(openSet) > 0 and currentNode != end):
            openSet.sort()
            openSet.reverse()
            currentNode = openSet.pop()
            closedSet.append(currentNode)

            if (currentNode == end):
                pathSuccess = True

            neighborList.clear()
            for myedge in currentNode.edges:
                neighborList.append(myedge)
            #neighborList = currentNode.edges
            for neighbor in neighborList:
                if type(neighbor) is edge:
                    if not neighbor.inObstacle:
                        neighborNode = neighbor.getOtherNode(currentNode)
                        if (not closedSet.__contains__(neighborNode)):
                            #newMovementCost = currentNode.gCost + currentNode.hCost
                            newMovementCost = currentNode.gCost + self.getDistance(currentNode,neighborNode)
                            if (newMovementCost < neighborNode.gCost or not openSet.__contains__(neighborNode)):
                                neighborNode.gCost = newMovementCost
                                neighborNode.hCost = self.getDistance(neighborNode, end)
                                neighborNode.parent = currentNode

                                if (not openSet.__contains__(neighborNode)):
                                    openSet.append(neighborNode)
                                    # else:
                                    # openSet.updateitem neighbor

        if pathSuccess:
            waypoints = self.tracePath(start, end)
            return waypoints
        else:
            return None

    def tracePath(self, start, end):
        path = []
        currentNode = end

        while currentNode != start:
            path.append(currentNode)
            currentNode = currentNode.parent
        path.append(start)
        path.reverse()
        return path

    def getDistance(self, a, b):
        x = math.fabs(a.x - b.x)
        y = math.fabs(a.y - a.y)
        return x + y

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
        edgeList = []
        for thisEdge in self.nodes:
            if(not edgeList.contains(thisEdge)):
                edgeList.append(thisEdge)
        self.edges = edgeList

    def resetMap(self):
        for thisEdge in self.edges:
            thisEdge.inObstacle = False

    def findEdge(self,name):
        for thisEdge in self.edges:
            if thisEdge.name == name:
                return thisEdge

    def findNode(self,name):
        for node in self.nodes:
            if(node.name == name):
                return node
        return None

    def getPath(self, start, end):
        mypath = path()
        mypath.nodes = self.__pathfinding(start, end)
        mypath.getPathAsStrings()
        return mypath

    # A* pathfinding solution
    def __pathfinding(self, start, end):
        # initialize components
        pathSuccess = False         #Assume there isn't a valid path
        openSet = []                #All new potential nodes to examine
        closedSet = []              #All nodes that have been previously examined
        neighborList = []           #The neighboring nodes to the current Node
        currentNode = Node('',0,0)  #the current node we are examining (default values)
        newMovementCost = 0         #The new cost to move to this location

        #put our start position in the openset to get started
        openSet.append(start)

        #WHILE there are nodes to process and we haven't found the end
        while (len(openSet) > 0 and not pathSuccess):
            #get the shortest distance node(also put it in the closed set)
            openSet.sort()
            for node in openSet:
                print(node.name)
            print("*****************")
            openSet.reverse()
            currentNode = openSet.pop(0)
            closedSet.append(currentNode)

            #if we found the end
            if (currentNode == end):
                #We're done
                pathSuccess = True
                break

            #get all the neighbors of the current node
            neighborList.clear()
            for myedge in currentNode.edges:
                neighborList.append(myedge)

            #for every nieghboring edge
            for neighbor in neighborList:
                #IF it is a real edge (it will be type string if not)
                if type(neighbor) is edge:
                    #also check if this is a traversable edge
                    if not neighbor.inObstacle:
                        #IF we haven't done this already
                        neighborNode = neighbor.getOtherNode(currentNode)
                        if (not closedSet.__contains__(neighborNode)):
                            #prep for the gCost
                            newMovementCost = currentNode.gCost + self.getDistance(currentNode,neighborNode)

                            #if there is no value or we have a better value
                            if (newMovementCost < neighborNode.gCost or not openSet.__contains__(neighborNode)):
                                #update the node's values
                                neighborNode.gCost = newMovementCost
                                neighborNode.hCost = self.getDistance(neighborNode, end)
                                neighborNode.parent = currentNode

                                #if it isn't in the open set, it should be
                                if (not openSet.__contains__(neighborNode)):
                                    openSet.append(neighborNode)

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
        return math.pow((x*x + y*y),.5)

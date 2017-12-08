from PathfindingRover.pathfinding.map import map
import json
from PathfindingRover.pathfinding.path import path
from PathfindingRover.pathfinding.robotPosition import RobotPosition
#from map import map
from PathfindingRover.pathfinding.Node import edge
from PathfindingRover.pathfinding.Node import Node

class UpdateData(object):

    def __init__(self,pos,inpath,inmap):
        self.myPath = inpath
        self.robpos = pos
        self.map = inmap

    # def toString(self):
    #     temp = 'Update '
    #     temp = temp + 'PathNodes '
    #     for node in self.mypath.nodes:
    #         temp = temp + node.name + ' '
    #     temp = temp + 'RobotNode ' + self.robpos.currentNode + ' '
    #     temp = temp + 'Edges '
    #     for thisEdge in map:
    #         temp = temp + thisEdge.name + ' ' + thisEdge.inObstacle + ' '
    #
    #     return temp

    def toString(self):
        nodelist = ''
        for node in self.myPath.nodes:
            nodelist = nodelist + node.name + ' '
        robotNode = self.robpos.currentNode
        edgelist = ''
        for thisEdge in self.map.edges:
            if(thisEdge.inObstacle):
                obstacle = "True"
            else:
                obstacle = "False"
            edgelist = edgelist + thisEdge.name + ' ' + obstacle + ' '
        # d = [["PathNodes",nodelist],["RobotNode", robotNode],["Edges", edgelist]]
        # d = {}
        # d['Path Nodes'] = nodelist
        # d['RobotNode'] = robotNode
        # d['Edges'] = edgelist
        # json_data = json.dumps(d);
        return nodelist.rstrip() + '/' + robotNode

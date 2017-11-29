from PathfindingRover.pathfinding.map import map
import json
from PathfindingRover.pathfinding.path import path
from PathfindingRover.pathfinding.robotPosition import RobotPosition
#from map import map
from Node import edge
from Node import Node

class UpdateData(object):

    def __init__(self,pos,inpath,map):
        self.myPath = inpath
        self.robpos = pos
        self.map = map

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

    def updatedJson(self):
        nodelist = ''
        for node in self.mypath.nodes:
            nodelist = nodelist + node.name + ' '
        robotNode = self.robpos.currentNode
        edgelist = ''
        for thisEdge in map:
            edgelist = edgelist + thisEdge.name + ' ' + thisEdge.inObstacle + ' '
        # d = [["PathNodes",nodelist],["RobotNode", robotNode],["Edges", edgelist]]
        # d = {}
        # d['Path Nodes'] = nodelist
        # d['RobotNode'] = robotNode
        # d['Edges'] = edgelist
        # json_data = json.dumps(d);
        return nodelist + '/' + robotNode + "/" + edgelist

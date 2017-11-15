from path import path
from robotPosition import RobotPosition
from map import map
from Node import edge
from Node import Node

class UpdateData(object):

    def __init__(self,pos,inpath,map):
        self.myPath = inpath
        self.robpos = pos
        self.map = map

    def toString(self):
        temp = 'Update '
        temp = temp + 'PathNodes '
        for node in self.mypath.nodes:
            temp = temp + node.name + ' '
        temp = temp + 'RobotNode ' + self.robpos.currentNode + ' '

        temp = temp + 'Edges '
        for thisEdge in map:
            temp = temp + thisEdge.name + ' ' + thisEdge.inObstacle + ' '

        return temp


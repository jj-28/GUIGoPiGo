from map import map
from Node import Node
from path import path
from robotPosition import RobotPosition
map = map()
readyToLeave = False

#while(readyToLeave):
    #prompt user

#TODO test obstacles
#TODO handle diagonal problem
robot = RobotPosition()
commands = []
start = input("Enter start location: ")
end = input("Enter end locastion: ")
startNode = map.findNode(start)
endNode = map.findNode(end)
#get the path
mypath = path()
mypath = map.getPath(startNode,endNode)


if mypath.nodes != None:
    mynodes = []
    myhcost = []

    #prep and print nodes
    for node in mypath.nodes:
        mynodes.append(node.name)
    print(mynodes)

    #prep and print all hcosts
    for node in map.nodes:
        myhcost.append(node.hCost)
    print(myhcost)

    #prep and print directions
    commands = mypath.getPathAsStrings(robot)
    print(commands)
else:
    print("No valid path")

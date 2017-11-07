from map import map
from Node import Node
from path import path
map = map()
readyToLeave = False

#while(readyToLeave):
    #prompt user
start = input("Enter start location: ")
end = input("Enter end locastion: ")
startNode = map.findNode(start)
endNode = map.findNode(end)
#get the path
mypath = path()
mypath = map.getPath(startNode,endNode)

for node in mypath.nodes:
    print(node.name)

for instruction in mypath.commands:
    print (instruction)

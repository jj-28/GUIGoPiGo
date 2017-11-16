from map import map
from path import path
from robotPosition import RobotPosition
ourMap = map()
outPath = path()
robotPosition = RobotPosition()
currentCommand = 'None'
node = None
while(True):
    #Check for new map
    #IF there is a new map
        #Clear everything and reset
        #update map and GUI to match
    #check rover status
    #IF rover is idle
        #ask for a node
        #IF node is available
            #get a new path
            #guichange is needed
    #ELIF rover is processing
        #Do nothing
    #ELIF waiting for next command
        #IF there are remaining commands
            #send next command
            #Gui change is needed
        #ELSE
            #set status to idle
    #check pathfinding status
    #IF current path is empty
    if len(path.nodes) == 0:
        #ask for next node
        node = 'Node'
        #IF there is a next node
        if node != None:
            #update map
            #pathfind
            myPath = map.getPath(map.findNode(robotPosition.currentNode),node)
            #Gui change is needed

    #check GUI status
    #IF GUI tells us to stop
        #stop, clear paths
    #IF there was any change
        #Tell GUI of change



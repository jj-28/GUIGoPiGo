import Node
import edge
import compassDirections
import robotPosition

class path(object):
    """description of class"""
    robotPos
    nodes[] #the nodes of a path
    commands[] #string of commands for robot controller

    #get a path of strings for the robot to use
    def getPathAsStrings()
        i = 0 #the node index
        j = 0 #directions index
        fakepos = robotPosition()
        fakepos.direction = robotpos.direction

        #WHILE we have not reached the end node
            #get the next node
            #IF not the first node
                #set robot direction opposite to direction it came
            #get the edge we are working with
            #WHILE we aren't facing the correct direction
                #get a direction to turn to


        #while we have nodes to process
        while(nodes.length > i)
            #get the next node
            node = nodes[i]

            #if not the first node
            if(not i = 0)
                #set robot direction opposite to direction it came
                edge = nodes[i-1].getEdge(nodes[i])
                tempDirection =  edge.getDirection(nodes[i])
                fakepos.direction = reverseDirection(tempDirection)
            #get the edge we need
            edge = nodes[i].getEdge(nodes[i+1])
            direction = edge.getDirection(node)
            #while we aren't facint the correct direction
            while(not fakepos.direction = direction )
                commands[j] = getDirection(direction,fakepos.direction)
                j++
            commands[j]= "Forward"
            #prep for next node
            i++
            j++


    def reverseDirection(d)
        if(d = north)
            return compassDirections.south
        else if(d = east)
            return compassDirections.west
        else if(d = west)
            return compassDirections.east
        else if(d = south)
            return compassDirections.north

    def getDirection(d1,d2)
        if(d1 = d2)
            return "TurnAround"
        if(d1 = compassDirections.north)
            if(d2 = compassDirections.east)
                return "Right"
            else if(d2 = compassDirections.west)
                return "Left"
        else if(d1 = compassDirections.east)
            if(d2 = compassDirections.north)
                return "Left"
            else if(d2 = compassDirections.south)
                return "Right"
        else if(d1 = compassDirections.south)
            if(d2 = compassDirections.east)
                return "Left"
            else if(d2 = compassDirections.west)
                return "Right"
        else if(d1 = compassDirections.west)
            if(d2 = compassDirections.south)
                return "Left"
            else if(d2 = compassDirections.north)
                return "Right"
            
            





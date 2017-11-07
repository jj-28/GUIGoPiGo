from Node import Node
from Node import edge
from compassDirections import compassDirections
class mapAssembler(object):
    """description of class
    this class will read the current map from a file for use in the project
    """
    fileName = ''#name of the file

    def assembleMap(self):
        map = []
        map.append(Node('n1',76,0))
        map.append(Node('n2',104,30))
        map.append(Node('n3',76,30))
        map.append(Node('n4',76,99))
        map.append(Node('n5',104,99))
        map.append(Node('n6',76,169))
        map.append(Node('n7',61,99))
        map.append(Node('n8',61,169))
        map.append(Node('n9',37,145))
        map.append(Node('n10',47,169))
        map.append(Node('n11',28,145))
        map.append(Node('n12',0,145))
        map.append(Node('n13',27,84))
        map.append(Node('n14',19,41))
        map.append(Node('n15',0,41))
        map.append(Node('n16',19,0))
        map.append(Node('n17',45,84))
        map.append(Node('n18',61,87))
        map.append(Node('n19',61,0))

        #to add an edge: call edge() its parameters are: the first node, the direction it connects at
        #then the second node and the direction it connects...followed by its weight and if an obstacle is present
        #(use 0 and false for now)
        #TODO: Needs redoing
        #CHANGED:
        #      edge(map[0].....,0,False)
        #              .
        #              .
        #              .
        #      edge(map[18]......,0,False)
        edge(map[0],compassDirections.north,map[1],compassDirections.south,0,False)
        edge(map[1],compassDirections.east,map[2],compassDirections.west,0,False)
        edge(map[1],compassDirections.north,map[3],compassDirections.south,0,False)
        edge(map[3],compassDirections.east,map[4],compassDirections.west,0,False)
        edge(map[3],compassDirections.north,map[5],compassDirections.south,0,False)
        edge(map[3],compassDirections.west,map[6],compassDirections.east,0,False)
        edge(map[6],compassDirections.north,map[7],compassDirections.south,0,False)
        edge(map[6],compassDirections.west,map[8],compassDirections.south,0,False)
        edge(map[8],compassDirections.east,map[9],compassDirections.south,0,False)
        edge(map[8],compassDirections.west,map[10],compassDirections.east,0,False)
        edge(map[10],compassDirections.west,map[11],compassDirections.east,0,False)
        edge(map[10],compassDirections.south,map[12],compassDirections.north,0,False)
        edge(map[12],compassDirections.west,map[13],compassDirections.north,0,False)
        edge(map[13],compassDirections.west,map[14],compassDirections.east,0,False)
        edge(map[13],compassDirections.south,map[15],compassDirections.north,0,False)
        edge(map[13],compassDirections.east,map[16],compassDirections.south,0,False)
        edge(map[16],compassDirections.west,map[12],compassDirections.east,0,False)
        edge(map[16],compassDirections.east,map[17],compassDirections.west,0,False)
        edge(map[17],compassDirections.north,map[6],compassDirections.south,0,False)
        edge(map[17],compassDirections.south,map[18],compassDirections.north,0,False)


        return map

        #
        #                                                __
        #                                               |_
        #                                               __)
        #                                                |
        #                                                |
        #                                                |
        #                                                |
        #                                                |
        #                                                |
        #                     _                          | __
        #                    |_                          | __)                     |_|
        #                    |_)   _____________________ | __)   __________________  |
        #                                                |
        #                                                |
        #                                                |
        #                                                |
        #                                                |
        #                                                |
        #                     __                         | __
        #                      /                         |  _)                        /|
        #                     /   ______________________ | /__   ____________________  |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |
        #                        |                                                   |    
        #                     _  |                                                   |  _
        #                    (_) |                                                   | / \
        #                    (_) | _________________________________________________ | \_/

        # Method for a second map made above
        def assembleMap2(self):
        # TODO Write a method which makes a square shape and all the edges
        # CHANGED

            map = []
            map[0]= Node('n1')
            map[1]= Node('n2')
            map[2]= Node('n3')
            map[3]= Node('n4')
            map[4]= Node('n5')
            map[5]= Node('n6')
            map[6]= Node('n7')
            map[7]= Node('n8')
            map[8]= Node('n9')
            map[9]= Node('n10')

            # CHANGED
            #
            #  Below are the edges for the square shape which conatains the nodes and direction on compass

            edge(map[0],compassDirections.north,map[1],compassDirections.south,0,False)
            edge(map[1],compassDirections.west,map[2],compassDirections.east,0,False)
            edge(map[2],compassDirections.north,map[3],compassDirections.south,0,False)
            edge(map[3],compassDirections.east,map[4],compassDirections.west,0,False)
            edge(map[3],compassDirections.north,map[5],compassDirections.south,0,False)
            edge(map[3],compassDirections.west,map[6],compassDirections.east,0,False)
            edge(map[5],compassDirections.south,map[6],compassDirections.north,0,False)
            edge(map[6],compassDirections.south,map[7],compassDirections.north,0,False)
            edge(map[7],compassDirections.east,map[2],compassDirections.west,0,False)
            edge(map[7],compassDirections.south,map[8],compassDirections.north,0,False)
            edge(map[8],compassDirections.east,map[0],compassDirections.west,0,False)


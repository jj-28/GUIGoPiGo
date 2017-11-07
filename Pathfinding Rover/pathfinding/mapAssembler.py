import Node
import edge
import compassDirections
class mapAssembler(object):
    """description of class
    this class will read the current map from a file for use in the project
    """
    fileName = ''#name of the file

    def assembleMap(self):
        map = []
        map[0]= Node('n1',76,0)
        map[1]= Node('n2',104,30)
        map[2]= Node('n3',76,30)
        map[3]= Node('n4',76,99)
        map[4]= Node('n5',104,99)
        map[5]= Node('n6',76,169)
        map[6]= Node('n7',61,99)
        map[7]= Node('n8',61,169)
        map[8]= Node('n9',37,145)
        map[9]= Node('n10',47,169)
        map[10]= Node('n11',28,145)
        map[11]= Node('n12',0,145)
        map[12]= Node('n13',27,84)
        map[13]= Node('n14',19,41)
        map[14]= Node('n15',0,41)
        map[15]= Node('n16',19,0)
        map[16]= Node('n17',45,84)
        map[17]= Node('n18',61,87)
        map[18]= Node('n19',61,0)

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
        edge(map[11],compassDirections.south,map[12],compassDirections.north,0,False)
        edge(map[12],compassDirections.south,map[13],compassDirections.north,0,False)
        edge(map[13],compassDirections.west,map[14],compassDirections.east,0,False)
        edge(map[13],compassDirections.south,map[15],compassDirections.north,0,False)
        edge(map[13],compassDirections.east,map[16],compassDirections.south,0,False)
        edge(map[16],compassDirections.west,map[12],compassDirections.east,0,False)
        edge(map[16],compassDirections.east,map[17],compassDirections.west,0,False)
        edge(map[17],compassDirections.north,map[6],compassDirections.south,0,False)
        edge(map[17],compassDirections.south,map[18],compassDirections.north,0,False)

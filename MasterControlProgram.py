from PathfindingRover.pathfinding.map import map
from PathfindingRover.pathfinding.path import path
from PathfindingRover.pathfinding.robotPosition import RobotPosition
#from RPi_Server_Code import WSHandler
import queue
import threading
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import time

#WSHandler = WSHandler().onmessage()



#Initialize TOrnado to use 'GET' and load index.html
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())
#Code for handling the data sent from the webpage
class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print ('connection opened...')
    def check_origin(self,origin):
        return True
    def on_message(self, message):
        print ('received:', message)
        Nodem = message
        currentCommand = 'None'
        node = None
        node = Nodem
        #if len(ourPath.nodes)==0 :
        temp = ''
        commandQueue.put(node)
        #temp = robotPosition.currentNode
        #temp = ourMap.findNode(temp)
        #node = ourMap.findNode(node)
        #ourPath = ourMap.getPath(temp,node,robotPosition)
        #for node in ourPath.nodes:
            #print(node.name)
        #print(ourPath.commands)

    #print ("Values Updated")
    def on_close(self):
        print ('connection closed...')

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue = queue
    def run(self):
        print ("Ready")
        application.listen(9093)            #starts the websockets connection
        tornado.ioloop.IOLoop.instance().start()
        while running:
            #      BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
            time.sleep(.2)              # sleep for 200 ms

if __name__ == "__main__":
    #BrickPiSetup()             # setup the serial port for communication
    #BrickPi.MotorEnable[PORT_A] = 1    #Enable the Motor A
    #BrickPi.MotorEnable[PORT_D] = 1    #Enable the Motor D
    #BrickPiSetupSensors()          #Send the properties of sensors to BrickPi
    ourMap = map()
    ourPath = path()
    robotPosition = RobotPosition()
    commandQueue = queue.Queue()
    running = True
    thread1 = myThread(1, "Thread-1", 1,commandQueue)
    thread1.setDaemon(True)
    thread1.start()

    global guiCall
    guiCall = ''
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
        #if len(ourPath.nodes) == 0:
        if not commandQueue.empty():
            #ask for next node
            node = commandQueue.get_nowait()
            #IF there is a next node
            if node != None and node != '':
                print (node)
                #update map
                #pathfind
                node = ourMap.findNode(node)
                ourPath = ourMap.getPath(ourMap.findNode(robotPosition.currentNode),node,robotPosition)
                for node in ourPath.nodes:
                    print(node.name)
                print(ourPath.commands)
                #Gui change is needed
                #check GUI status
        #IF GUI tells us to stop
            #stop, clear paths
        #IF there was any change
            #Tell GUI of change
        time.sleep(.2)
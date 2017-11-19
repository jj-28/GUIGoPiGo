from PathfindingRover.pathfinding.map import map
from PathfindingRover.pathfinding.path import path
from PathfindingRover.pathfinding.robotPosition import RobotPosition
from RobotController.src.Wrapper import *
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
        node = Nodem
        commandQueue.put(node)
        if not guiMessageQueue.empty():
            #send message back up.
            pass


    #print ("Values Updated")
    def on_close(self):
        print ('connection closed...')

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])

class guiControlThread (threading.Thread):
    def __init__(self, threadID, name, counter, cqueue, queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue = queue
        self.cqueue = cqueue
    def run(self):
        print (self.name + " Ready")
        application.listen(9093)            #starts the websockets connection
        tornado.ioloop.IOLoop.instance().start()

class robotControlThread(threading.Thread):
    def __init__(self, threadID, name, counter,cqueue,queue,control):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue = queue
        self.cqueue = cqueue
        self.control = control
    def run(self):
        print (self.name + " Ready")
        while (True):
            if not queue.empty():
                temp = queue.get()
                if temp == "Forward":
                    self.control.go_straight()
                elif temp == "Left":
                    self.control.turn_left()
                elif temp == "Right":
                    self.control.turn_right()
                elif temp == "TurnAround":
                    self.control.turn_around()
            time.sleep(.2)#note for commit

class mapRecievingThread(threading.Thread):
    def __init__(self, threadID, name, counter, cqueue, queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue = queue
        self.cqueue = cqueue
    def run(self):
        print (self.name + " Ready")

if __name__ == "__main__":
    ourMap = map()
    ourPath = path()
    robotPosition = RobotPosition()
    robotController = Wrapper()
    robotController.waiting = 2
    commandQueue = queue.Queue()
    guiMessageQueue = queue.Queue()
    rcMessageQueue = queue.Queue()

    #get threads going
    guiThread = guiControlThread(1, "Gui Control Thread", 1,commandQueue,guiMessageQueue)
    robotThread = robotControlThread(2,"Robot Control Thread",1,commandQueue,rcMessageQueue,robotController)
    guiThread.setDaemon(True)
    guiThread.start()
    robotThread.start()

    #main operating loop
    while(True):
        #Check for new map
        #IF there is a new map
            #Clear everything and reset
            #update map and GUI to match

        #check rover status
        #IF rover is idle
        if robotController.waiting == 2:
            #ask for a node
            if len(ourPath.nodes) > 0:
                robotController.waiting = 0
            #IF node is available
                #get a new path
                #guichange is needed
        #ELIF rover is processing
        if robotController.waiting == 0:
            pass
        #ELIF waiting for next command
        elif robotController.waiting == 1:
            #IF there are remaining commands
            if len(ourPath.commands) > 0:
                #send next command
                temp = ourPath.commands.pop(0)
                robotControlThread.put(temp)
                if temp == "Forward":
                    robotPosition.currentNode = ourPath.nodes.pop(0)
                #Gui change is needed
            #ELSE
            else:
                #set status to idle
                robotController.waiting = 2

        #check pathfinding status
        #IF current path is empty
        if len(ourPath.nodes) == 0:
            if not commandQueue.empty():
                #ask for next node
                node = commandQueue.get_nowait()
                #IF there is a next node
                if node != None and node != '':
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
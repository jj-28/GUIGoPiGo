from PathfindingRover.pathfinding.map import map
from PathfindingRover.pathfinding.path import path
from PathfindingRover.pathfinding.robotPosition import RobotPosition
from RobotController.src.RobotController import RobotController
from UpdateData import UpdateData
import queue
import threading
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import time
import json


# WSHandler = WSHandler().onmessage()

# global c
# c = False
#

# Initialize TOrnado to use 'GET' and load index.html
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())


# Code for handling the data sent from the webpage
class WSHandler(tornado.websocket.WebSocketHandler):
    # def senddict(self):
    #     if c is True:
    #         self.write_message(updates)
    #         else:

    def open(self):
        print('connection opened...')

    def check_origin(self, origin):
        return True

    def on_message(self, message):
        print("from client ", message)
        if message == "client ready":
            self.write_message('request initial node and edges')
            #print("from client", message)
        elif message == "request path":
            if not guiMessageQueue.empty():
                order = guiMessageQueue.get_nowait()
                print ("path being sent back  up ",order)
                self.write_message(order)
        else:
            print("command queue now has: " + message)
            commandQueue.put(message)
##            if not guiMessageQueue.empty():
##                order = guiMessageQueue.get_nowait()
##                print ("path being sent back  up ",order)
##                self.write_message(order)
            # assign edges to relevant function for pathfinding input

    def on_close(self):
        print('connection closed...')
    def sendup (self):
        if not guiMessageQueue.empty():
                print ("path being sent back  up ",guiMessageQueue.get_nowait())
                self.write_message(guiMessageQueue.get_nowait())

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])


class guiControlThread(threading.Thread):
    def __init__(self, threadID, name, counter, cqueue, queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue = queue
        self.cqueue = cqueue

    def run(self):
        print(self.name + " Ready\n")
        application.listen(9093)  # starts the websockets connection
        tornado.ioloop.IOLoop.instance().start()


class robotControlThread(threading.Thread):
    def __init__(self, threadID, name, counter, cqueue, queue, control):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue = queue
        self.cqueue = cqueue
        self.control = control

    def run(self):
        print(self.name + " Ready\n")
        while (True):
            if not self.queue.empty():
                temp = self.queue.get()
                robotController.status = "processing"
                print("processing: " + temp)
                if temp == "Forward":
                    robotController.follow_line()
                elif temp == "Left":
                    robotController.turn_left()
                elif temp == "Right":
                    robotController.turn_right()
                elif temp == "TurnAround":
                    robotController.turn_around()
                robotController.status = "waiting"
                print("awaiting orders")
            time.sleep(1)  # note for commit


class mapRecievingThread(threading.Thread):
    def __init__(self, threadID, name, counter, cqueue, queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.queue = queue
        self.cqueue = cqueue

    def run(self):
        print(self.name + " Ready")


if __name__ == "__main__":
    ourMap = map()
    ourPath = path()

    robotPosition = RobotPosition()
    robotController = RobotController()
    robotController.waiting = 2
    commandQueue = queue.Queue()
    guiMessageQueue = queue.Queue()
    rcMessageQueue = queue.Queue()
    node = None
    # idk if right
    # get threads going
    print("Starting threads")
    guiThread = guiControlThread(1, "Gui Control Thread", 1, commandQueue, guiMessageQueue)
    robotThread = robotControlThread(2, "Robot Control Thread", 1, commandQueue, rcMessageQueue, robotController)
    guiThread.setDaemon(True)
    guiThread.start()
    robotThread.start()

    # main operating loop
    while (True):
        # Check for new map
        # IF there is a new map
        # Clear everything and reset
        # update map and GUI to match

        # check rover status
        # IF rover is idle
        if robotController.status == "idle":
            # ask for a node
            if len(ourPath.nodes) > 0:
                robotController.status = "processing"
                if len(ourPath.commands)>0:
                    temp= ourPath.commands.pop(0)
                    rcMessageQueue.put(temp)
                    if temp == "Forward":
                        guiMessageQueue.put(robotPosition.currentNode)
                        robotPosition.currentNode = ourPath.nodes.pop(0).name
                        print("forward Position" + robotPosition.currentNode)
                        
                # IF node is available
                # get a new path
                # guichange is needed
        # ELIF rover is processing
        if robotController.status == "processing":
            pass
        # ELIF waiting for next command
        elif robotController.status == "waiting":
            # IF there are remaining commands
            if len(ourPath.commands) > 0:
                # send next command
                temp = ourPath.commands.pop(0)
                rcMessageQueue.put(temp)
                print("incoming command: " + temp)
                robotController.status = "processing"
                if temp == "Forward":
                    robotPosition.currentNode = ourPath.nodes.pop(0).name
                    print("forward Position" + robotPosition.currentNode)
                    guiMessageQueue.put(robotPosition.currentNode)
                    #ourPath.nodes.pop(0)
                    # Gui change is needed
            # ELSE
            else:
                # set status to idle
                robotController.status = "idle"
                print("all orders completed, robot is idle")
                ourPath = path()
                ourPath.nodes = []
                ourPath.edges = []
                print(robotPosition.currentNode)
                #updates = UpdateData(robotPosition,ourPath,ourMap)
                guiMessageQueue.put(robotPosition.currentNode)
                guiMessageQueue.put("PATH COMPLETE")
                
        # check pathfinding status
        # IF current path is empty
        if len(ourPath.nodes) == 0 and robotController.status == "idle":
            if not commandQueue.empty():
                hashstring = commandQueue.get_nowait()
                print(hashstring)
                node = hashstring.split("/")[0]
                print(node)
                if len(hashstring.split("/")) > 1:
                    edges = hashstring.split("/")[1].split(" ")  # ask for next node
                    #print(edges)
                    ourMap.resetMap()
                #if edges != None:
                    for name in edges:
                        print("edge", name)
                        offedge = ourMap.findEdge(name)
                        offedge.inObstacle = True
                while not commandQueue.empty():
                    commandQueue.get()
            # IF there is a next node
            if node != None and node != '':
            # update map
            # pathfind
                mapnode = ourMap.findNode(node)
                ourPath = ourMap.getPath(ourMap.findNode(robotPosition.currentNode), mapnode, robotPosition)
                if ourPath.nodes != None:
                    for node in ourPath.nodes:
                        #print(node.name)
                        print(ourPath.commands)
                    print("Robot Position: " +robotPosition.currentNode)
                    robotPosition.currentNode = ourPath.nodes.pop(0).name
                    print("Robot Position new: " +robotPosition.currentNode)
                    updates = UpdateData(robotPosition,ourPath,ourMap)
                    print (updates.toString())
                    guiMessageQueue.put(updates.toString())
                else:
                    guiMessageQueue.put("ERROR")
                    ourPath = path()
                    ourPath.nodes = None
                node = None
            # Gui change is needed

            # check GUI status
            # IF GUI tells us to stop
            # stop, clear paths
            # IF there was any change
            # Tell GUI of change
        time.sleep(1.2)

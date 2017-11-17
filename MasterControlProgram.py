from map import map
from path import path
from robotPosition import RobotPosition
from RPi_Server_Code import WSHandler

import threading
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import time
ourMap = map()
ourPath = path()
robotPosition = RobotPosition()
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
        ourPath = map.getPath(map.findNode(robotPosition.currentNode),node)
        print(ourPath.nodes)
        print(ourPath.commands)

    #print ("Values Updated")
    def on_close(self):
        print ('connection closed...')

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r'/', MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Ready")
        while running:
            #      BrickPiUpdateValues()       # Ask BrickPi to update values for sensors/motors
            time.sleep(.2)              # sleep for 200 ms

if __name__ == "__main__":
    #BrickPiSetup()             # setup the serial port for communication
    #BrickPi.MotorEnable[PORT_A] = 1    #Enable the Motor A
    #BrickPi.MotorEnable[PORT_D] = 1    #Enable the Motor D
    #BrickPiSetupSensors()          #Send the properties of sensors to BrickPi
    running = True
    thread1 = myThread(1, "Thread-1", 1)
    thread1.setDaemon(True)
    thread1.start()
    application.listen(9093)            #starts the websockets connection
    tornado.ioloop.IOLoop.instance().start()
    node = on_message().Nodem()

# from map import map
# from path import path
# from robotPosition import RobotPosition
# from socketcmdline import transfer
# ourMap = map()
# ourPath = path()
# robotPosition = RobotPosition()
# transfer = transfer()
# currentCommand = 'None'
# node = None
# while(True):
#     #Check for new map
#     #IF there is a new map
#         #Clear everything and reset
#         #update map and GUI to match
#     #check rover status
#     #IF rover is idle
#         #ask for a node
#         #IF node is available
#             #get a new path
#             #guichange is needed
#     #ELIF rover is processing
#         #Do nothing
#     #ELIF waiting for next command
#         #IF there are remaining commands
#             #send next command
#             #Gui change is needed
#         #ELSE
#             #set status to idle
#     #check pathfinding status
#     #IF current path is empty
#     if len(path.nodes) == 0:
#         #ask for next node
#         print
#         transfer
#         node = transfer
#         #IF there is a next node
#         if node != None:
#             #update map
#             #pathfind
#             ourPath = map.getPath(map.findNode(robotPosition.currentNode),node)
#             print(ourPath.nodes)
#             print(ourPath.commands)
#             #Gui change is needed
#
#     #check GUI status
#     #IF GUI tells us to stop
#         #stop, clear paths
#     #IF there was any change
#         #Tell GUI of change
#
#

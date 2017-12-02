'''
Created on Nov 17, 2017

@author: Charles
'''
from easygopigo1 import *
from gopigo import *
import time

class Wrapper(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.gpg = EasyGoPiGo()
        self.ls = LineFollower()
        self.waiting = 1
        # speed is set to 30
        self.gpg.set_speed(30)
        #self.ls.calibrateSensors()
        self.ls.new_read()
        self.ls.new_read()

    # follows line straight
    def getwaiting(self):
        return self.waiting
        
    def waiting(self):
        status = self.getwaiting()
        return status

    def t_intersection(self):
        print("T-intersection found")
        
    def followline(self):
        self.waiting = 0
        self.ls.rfollow_line()
        self.waiting = 1
        
    def go_straight(self):
        print("Going straight")
        self.waiting = 0
        self.gpg.forward()
        #time.sleep(.8)
        self.ls.follow_line()
        self.waiting = 1
        
    def turn_right(self):
        print("Turning right")
        self.waiting = 0
        self.ls.turn_right()
        self.waiting = 1
        
    def turn_left(self):
        print("Turning left")
        self.waiting = 0
        self.ls.turn_left()
        self.waiting = 1
        
    def turn_around(self):
        print("Turning around")
        self.waiting = 0
        self.ls.turn_around()
        time.sleep(.1)
        self.ls.follow_line()
        self.waiting = 1

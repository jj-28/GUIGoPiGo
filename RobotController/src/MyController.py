'''
Created on Oct 29, 2017

@author: Charles
'''
from __future__ import print_function
from __future__ import division

import sys
import time
import math
import struct
import subprocess



try:
    
    from gopigo import *
except ImportError:
    hardware_connected = False
    print("Cannot import gopigo library")
    
DPR = 360.0/64    

#Move the GoPiGo forward
def gofwd(dist=0): #distance is in cm
    try:
        if dist>0:
            # this casting to int doesn't seem necessary
            pulse=int(PPR*(dist//WHEEL_CIRC) )
            enc_tgt(1,1,pulse)
    except Exception as e:
        print ("gopigo fwd: {}".format(e))
        pass
    return write_i2c_block(address,motor_fwd_cmd+[0,0,0])

def rotate_left():
    return write_i2c_block(address,left_rot_cmd+[0,0,0])

def rotate_right():
    return write_i2c_block(address,right_rot_cmd+[0,0,0])

def turn_right(degrees):
    pulse = int(degrees//DPR)
    enc_tgt(1,0,pulse)
    right()
    
def turn_right_wait_for_completion(degrees):
    '''
    Same as turn_right() but blocking
    '''
    turn_right(degrees)
    pulse = int(degrees//DPR)
    while enc_read(0) < pulse:
        pass
    
def turn_left(degrees):
    pulse = int(degrees//DPR)
    enc_tgt(0,1,pulse)
    left()
    
def turn_left_wait_for_completion(degrees):
    '''
    same as turn_left() but blocking.
    '''
    turn_left(degrees)
    pulse = int(degrees//DPR)
    while enc_read(1) < pulse:
        pass
    
##################################
def get_speed():
    print(read_motor_speed_cmd)
    speeds = read_motor_speed()
    sp1 = speeds[1]
    sp2 = speeds[0]
    print("speed left:")
    print(sp1)
    print("speed right:")
    print(sp2)
    
def decrease_left():
    speeds = read_motor_speed()
    sp1 = speeds[1]
    sp1 = sp1 - 10
    set_left_speed(sp1)
    
def decrease_right():
    speeds = read_motor_speed()
    sp2 = speeds[0]
    sp2 = sp2 - 10
    set_right_speed(sp2)
    

    

    
    
#def rotate_test_r(degrees):
    

#######################3
try:
    PORTS = {"A1": gopigo.analogPort, "D11": gopigo.digitalPort,
             "SERIAL": -1, "I2C": -2, "SERVO": -3}
except:
    PORTS = {"A1": 15, "D11": 10, "SERIAL": -1, "I2C": -2, "SERVO": -3}


ANALOG = 1
DIGITAL = 0
SERIAL = -1
I2C = -2
########################3


class Sensor():
    '''
    Base class for all sensors
    Class Attributes:
        port : string - user-readable port identification
        portID : integer - actual port id
        pinmode : "INPUT" or "OUTPUT"
        pin : 1 for ANALOG, 0 for DIGITAL
        descriptor = string to describe the sensor for printing purposes
    Class methods:
        setPort / getPort
        setPinMode / getPinMode
        isAnalog
        isDigital
    '''
    def __init__(self, port, pinmode):
        '''
        port = one of PORTS keys
        pinmode = "INPUT", "OUTPUT", "SERIAL" (which gets ignored), "SERVO"
        '''
        debug("Sensor init")
        debug(pinmode)
        self.setPort(port)
        self.setPinMode(pinmode)
        if pinmode == "INPUT" or pinmode == "OUTPUT":
            try:
                gopigo.pinMode(self.getPortID(), self.getPinMode())
            except:
                pass

    def __str__(self):
        return ("{} on port {}".format(self.descriptor, self.getPort()))

    def setPort(self, port):
        self.port = port
        self.portID = PORTS[self.port]

    def getPort(self):
        return (self.port)

    def getPortID(self):
        return (self.portID)

    def setPinMode(self, pinmode):
        self.pinmode = pinmode

    def getPinMode(self):
        return (self.pinmode)

    def isAnalog(self):
        return (self.pin == ANALOG)

    def isDigital(self):
        return (self.pin == DIGITAL)

    def set_descriptor(self, descriptor):
        self.descriptor = descriptor

#########################################

class LineFollower(Sensor):
    '''
    The line follower detects the presence of a black line or its
      absence.
    You can use this in one of three ways.
    1. You can use read_position() to get a simple position status:
        center, left or right.
        these indicate the position of the black line.
        So if it says left, the GoPiGo has to turn right
    2. You can use read() to get a list of the five sensors.
        each position in the list will either be a 0 or a 1
        It is up to you to determine where the black line is.
    3. You can use read_raw_sensors() to get raw values from all sensors
        You will have to handle the calibration yourself
    4. the gpg argument is ignored. Needed for future compatibility
    '''

    def __init__(self, port="I2C", pinmode="",gpg=None):
        try:
            Sensor.__init__(self, port, "INPUT")
            self.set_descriptor("Line Follower")
            self.last_3_reads = []
            self.white_line = self.get_white_calibration()
            self.black_line = self.get_black_calibration()
            self.threshold = [w+((b-w)/2) for w,b in zip(self.white_line,self.black_line)]
        except:
            raise ValueError("Line Follower Library not found")

    def read_raw_sensors(self):
        '''
        Returns raw values from all sensors
        From 0 to 1023
        May return a list of -1 when there's a read error
        '''

        _grab_read()
        try:
            five_vals = line_sensor.read_sensor()
        except:
            pass
        _release_read()
        debug ("raw values {}".format(five_vals))

        if five_vals != -1:
            return five_vals
        else:
            return [-1, -1, -1, -1, -1]

    def get_white_calibration(self):
        return line_sensor.get_white_line()

    def get_black_calibration(self):
        return line_sensor.get_black_line()

    def read(self):
        '''
        Returns a list of 5 values between 0 and 1
        Depends on the line sensor being calibrated first
            through the Line Sensor Calibration tool
        May return all -1 on a read error
        '''

        five_vals = [-1,-1,-1,-1,-1]


        five_vals = self.read_raw_sensors()

        line_result = []
        for sensor_reading,cur_threshold in zip(five_vals,self.threshold):
            if sensor_reading > cur_threshold:
                line_result.append(1)
            else:
                line_result.append(0)

        debug ("Current read is {}".format(line_result))

        if five_vals != [-1,-1,-1,-1,-1]:
            debug("appending")
            self.last_3_reads.append(line_result)
        if len(self.last_3_reads) > 3:
            self.last_3_reads.pop(0)

        debug (self.last_3_reads)
        transpose = list(zip(*self.last_3_reads))
        avg_vals = []
        for sensor_reading in transpose:
            # print (sum(sensor_reading)//3)
            avg_vals.append(sum(sensor_reading)//3)

        debug ("current avg: {}".format(avg_vals))
        return avg_vals

    def follow_line(self,fwd_speed=80):
        slight_turn_speed=int(.7*fwd_speed)
        while True:
            pos = self.read_position()
            debug(pos)
            if pos == "center":
                gopigo.forward()
            elif pos == "left":
                gopigo.set_right_speed(0)
                gopigo.set_left_speed(slight_turn_speed)
            elif pos == "right":
                gopigo.set_right_speed(slight_turn_speed)
                gopigo.set_left_speed(0)
            elif pos == "black":
                gopigo.stop()
            elif pos == "white":
                gopigo.stop()

    def read_position(self):
        '''
        Returns a string telling where the black line is, compared to
            the GoPiGo
        Returns: "Left", "Right", "Center", "Black", "White"
        May return "Unknown"
        This method is not intelligent enough to handle intersections.
        '''
        five_vals = self.read()

        if five_vals == [0, 0, 1, 0, 0] or five_vals == [0, 1, 1, 1, 0]:
            return "center"
        if five_vals == [1, 1, 1, 1, 1]:
            return "black"
        if five_vals == [0, 0, 0, 0, 0]:
            return "white"
        if five_vals == [0, 1, 1, 0, 0] or \
           five_vals == [0, 1, 0, 0, 0] or \
           five_vals == [1, 0, 0, 0, 0] or \
           five_vals == [1, 1, 0, 0, 0] or \
           five_vals == [1, 1, 1, 0, 0] or \
           five_vals == [1, 1, 1, 1, 0]:
            return "left"
        if five_vals == [0, 0, 0, 1, 0] or \
           five_vals == [0, 0, 1, 1, 0] or \
           five_vals == [0, 0, 0, 0, 1] or \
           five_vals == [0, 0, 0, 1, 1] or \
           five_vals == [0, 0, 1, 1, 1] or \
           five_vals == [0, 1, 1, 1, 1]:
            return "right"
        return "unknown"

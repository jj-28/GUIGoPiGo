import sys
import time

try:
    import gopigo
except:
    pass
# import os

# the following libraries may or may not be installed
# nor needed
try:
    from I2C_mutex import *
except:
    pass

try:
    from line_follower import line_sensor
    from line_follower import scratch_line
    is_line_follower_accessible = True
except:
    try:
        sys.path.insert(0, '/home/pi/GoPiGo/Software/Python/line_follower')
        import line_sensor
        import scratch_line
        is_line_follower_accessible = True
    except:
        is_line_follower_accessible = False

old_settings = ''
fd = ''
##########################

read_is_open = True
global_lock = None

def debug(in_str):
    if False:
        print(in_str)


def _grab_read():
    '''
    first acquire at the process level,
    then at the thread level.
    '''
    global read_is_open
    # print("acquiring")
    try:
        I2C_Mutex_Acquire()
    except Exception as e:
        print("_grab_read: {}".format(e))
        pass
    # while read_is_open is False:
    #     time.sleep(0.01)
    read_is_open = False
    # print("acquired")


def _release_read():
    global read_is_open
    try:
        I2C_Mutex_Release()
    except Exception as e:
        print("_release_read: {}".format(e))
        pass
    read_is_open = True
    # print("released")


class EasyGoPiGo():
    '''
    Wrapper to access the gopigo functionality with mutex in place
    this makes the gopigo thread safe and process safe
    if mutex is not available, then it's just a direct access to gopigo
    '''
    def __init__(self):
        '''
        On Init, set speed to half-way, so GoPiGo is predictable
            and not too fast.
        '''
        DEFAULT_SPEED = 128
        gopigo.set_speed(DEFAULT_SPEED)

    def volt(self):
        _grab_read()
        try:
            voltage = gopigo.volt()
        except:
            voltage = 0
        _release_read()
        return voltage

    def stop(self):
        # no locking is required here
        try:
            gopigo.stop()
        except:
            pass

    def forward(self):
        _grab_read()
        try:
            val = gopigo.forward()
        except Exception as e:
            print("easygopigo fwd: {}".format(e))
            pass
        _release_read()


    def rotate_right(self):
        _grab_read()
        try:
            gopigo.set_right_speed(0)
            gopigo.set_left_speed(25)
        except Exception as e:
            print("idk wtf")
            pass

    def rotate_left(self):
        _grab_read()
        try:
            gopigo.set_right_speed(25)
            gopigo.set_left_speed(0)
        except Exception as e:
            print("idk wtf")
            pass


    def backward(self):
        _grab_read()
        try:
            val = gopigo.backward()
        except Exception as e:
            print("easygopigo bwd: {}".format(e))
            pass
        _release_read()

    def back10(self):
        _grab_read()
        try:
            val = gopigo.backward()
            time.sleep(1)
            val = gopigo.stop()
        except Exception as e:
            print("easygopigo bwd: {}".format(e))
            pass
        _release_read()

    def left(self):
        _grab_read()
        try:
            gopigo.left()
        except:
            pass
        _release_read()

    def right(self):
        _grab_read()
        try:
            gopigo.right()
        except:
            pass
        _release_read()

    def set_speed(self,new_speed):
        _grab_read()
        try:
            gopigo.set_speed(new_speed)
        except:
            pass
        _release_read()

    def reset_speed(self):
        _grab_read()
        try:
            gopigo.set_speed(DEFAULT_SPEED)
        except:
            pass
        _release_read()

    def set_left_speed(self,new_speed):
        _grab_read()
        try:
            gopigo.set_left_speed(new_speed)
        except:
            pass
        _release_read()

    def set_right_speed(self,new_speed):
        _grab_read()
        try:
            gopigo.set_right_speed(new_speed)
        except:
            pass
        _release_read()

    def trim_read(self):
        _grab_read()
        try:
            current_trim = int(gopigo.trim_read())
        except:
            pass
        _release_read()
        return current_trim

    def trim_write(self,set_trim_to):
        _grab_read()
        try:
            gopigo.trim_write(int(set_trim_to))
        except:
            pass
        _release_read()

#############################################################
# the following is in a try/except structure because it depends
# on the date of gopigo.py
#############################################################
try:
    PORTS = {"A1": gopigo.analogPort, "D11": gopigo.digitalPort,
             "SERIAL": -1, "I2C": -2, "SERVO": -3}
except:
    PORTS = {"A1": 15, "D11": 10, "SERIAL": -1, "I2C": -2, "SERVO": -3}


ANALOG = 1
DIGITAL = 0
SERIAL = -1
I2C = -2

##########################


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
##########################


##########################


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

    # turns left until center is read on the line reader
    def turn_left(self):
        gopigo.set_right_speed(25)
        gopigo.set_left_speed(0)
        gopigo.forward()
        time.sleep(2)
        while True:

            self.read_position()
            self.read_position()
            self.read_position()
            pos = self.read_position()
            print(pos)
            debug(pos)
            if pos == "center":
                gopigo.stop()
                break
    # turns right until center is read on the line reader
    def turn_right(self):
        gopigo.set_right_speed(0)
        gopigo.set_left_speed(25)
        gopigo.forward()
        time.sleep(2)
        while True:

            self.read_position()
            self.read_position()
            self.read_position()
            pos = self.read_position()
            print(pos)
            debug(pos)
            if pos == "center":
                gopigo.stop()
                break

    #Not completed (will turn forever)
    def turn_right_around(self):
        gopigo.set_right_speed(0)
        gopigo.set_left_speed(50)
        time.sleep(5)

    # Follow line reads position and moves accordingly.
    # Follows the line and prints where the GoPiGo is relative to the line, then prints to the
    # user the value at which it is located which is then used to center itself or stop.
    def follow_line(self,fwd_speed=30):
        slight_turn_speed=int(35)
        print("FOLLOWING LINE")
        while True:
            self.read_position()
            self.read_position()
            #print(self.read())
            pos = self.read_position()
            #print(pos)

            debug(pos)
            if pos == "center":
                gopigo.set_speed(30)
                gopigo.forward()
            elif pos == "wayleft":
                gopigo.set_right_speed(25)
                gopigo.set_left_speed(40)
            elif pos == "wayright":
                gopigo.set_right_speed(40)
                gopigo.set_left_speed(25)
            elif pos == "left":
                gopigo.set_right_speed(25)
                gopigo.set_left_speed(slight_turn_speed)
            elif pos == "right":
                gopigo.set_right_speed(slight_turn_speed)
                gopigo.set_left_speed(25)
            elif pos == "white":
                print("white Brake")
                gopigo.stop()
                break
            elif pos == "intersection":
                gopigo.stop()
                break
            elif pos == "unknown":
                print("Unknown???")
                gopigo.stop()
                break
            else:
                break

    def read_position(self):

        '''
        Returns a string telling where the black line is, compared to
            the GoPiGo
        Returns: "center", "black", "white", "intersection", "left", "right", "wayleft", or "wayright"
        May return "Unknown"
        '''
        five_vals = self.read()

        if five_vals == [0, 0, 1, 0, 0] or five_vals == [0, 1, 1, 1, 0]:
            return "center"
        if five_vals == [0, 0, 0, 0, 0]:
            return "white"
        if five_vals == [0, 1, 1, 1, 1] or \
           five_vals == [0, 0, 1, 1, 1] or \
           five_vals == [0, 0, 0, 1, 1] or \
           five_vals == [1, 1, 0, 0, 0] or \
           five_vals == [1, 1, 1, 1, 0] or \
           five_vals == [1, 1, 1, 1, 1] or \
           five_vals == [0, 1, 1, 0, 1] or \
           five_vals == [1, 0, 1, 1, 0] or \
           five_vals == [1, 1, 1, 0, 0]:
            return "intersection"
        if five_vals == [0, 1, 1, 0, 0] or \
           five_vals == [0, 1, 0, 0, 0]:
            return "left"
        if five_vals == [0, 0, 0, 1, 0] or \
           five_vals == [0, 0, 1, 1, 0]:
            return "right"
        if five_vals == [1, 0, 0, 0, 0]:
            return "wayleft"
        if five_vals == [0, 0, 0, 0, 1]:
            return "wayright"
        return "unknown"


import time     # import the time library for the sleep function
#import queue   

from gopigo import *
from MyController import *

'''
Create basic functions for the GPG. Enable ability to accept Queue of commands.
Create a socket to enable a connection with the server.
'''

def Main():
    
    
    
    
    
    print("Starting controller")
    print("CMDS: stop, forward, backward, rotations, rotater, rotatel, slowleft, slowright, status, exit")
    
    wheelone = 0
    wheeltwo = 0
    
    set_speed(100)
    
    while True:
        
        userin = raw_input()
        
        if userin == "stop":
            print ("stopping")
            stop()
            
        elif userin == "rotations":
            print("The left wheel has gone: ")
            print(enc_read(0))
            print("The right wheel has gone: ")
            print(enc_read(1))
            
        elif userin == "slowleft":
            decrease_left()
            
        elif userin == "slowright":
            decrease_right()
        
        elif userin == "rotater":
            print("rotating right")
            turn_right_wait_for_completion(90)
            stop()
            
        elif userin == "rotatel":
            print("rotating left")
            turn_left_wait_for_completion(90)
            stop()
            
        elif userin == "status":
            print("Current battery voltage:")
            print(volt())
            print("Current motor speed")
            get_speed()
        
        elif userin == "test1":
            print("testing")
        
        elif userin == "test2":
            print("testing2")
        
        elif userin == "forward":
            print("going forward\n")
            fwd()
    
        elif userin == "back":
            print("backwards\n")
            bwd()
            
        elif userin == "speed":
            print(read_motor_speed());
            
            
            
        elif userin == "exit":
            print("Exiting\n")
            sys.exit()
            break
            
        time.sleep(.1)
        
if __name__ == '__main__':
    Main()
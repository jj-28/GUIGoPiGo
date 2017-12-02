from __future__ import print_function
from __future__ import division
# from builtins import input

import sys
# import tty
# import select
import time
hardware_connected = True
try:
    from easygopigo import *
except ImportError:
    print("cannot improt EASYgopigo")

try:
    
    from gopigo import *
except ImportError:
    hardware_connected = False
    print("Cannot import gopigo library")
except Exception as e:
    hardware_connected = False
    print("Unknown issue while importing gopigo")
    print(e)
    
#import queue

class MyGoPiGo(easygopigo.EasyGoPiGo):
    

    def __init__(self):
        super(self.__class__, self).__init__()
        
        
    
import time
from RobotController import RobotController
import sys

rc = RobotController()
rc.read()

print("Starting controller")
print("CMDS: stop, rotations, status, exit")
print("MVMT CMDS: read, followline, turnaround, turnright, turnleft")

# Starts loop then prompts user for input then goes to sleep until next command is entered
while True:

    userin = input("command: ")

    if userin == "stop":
        print ("stopping")
        rc.stop()
            
    elif userin == "turnaround":
        print("turning around")
        rc.turn_around()

    elif userin == "turnright":
        print("right turn")
        rc.turn_right()

    elif userin == "turnleft":
        print("left turn")
        rc.turn_left()

    elif userin == "read":
        print("READING")
        print(rc.read())

    elif userin == "followline":
        rc.follow_line()

    elif userin == "status":
        print("Current battery voltage:")
        print(rc.volt())

    elif userin == "exit":
        print("Exiting\n")
        sys.exit()
        break

    time.sleep(.1)

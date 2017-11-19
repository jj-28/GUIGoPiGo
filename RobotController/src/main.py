# import the time library for the sleep function
import time
from gopigo import *
from easygopigo1 import *
from Wrapper import *

def Main():

    # instanstiated in order to use methods
    gpg = EasyGoPiGo()
    ls = LineFollower()
    wrapper = Wrapper()
    
    # line sensor reads the current position on the line twice for accuracy
    ls.read()
    ls.read()

    print("Starting controller")
    print("CMDS: stop, rotations, status, exit")
    print("GPG3: read, speed, followline, rp, turnright, turnleft")
    print("Wrapper: wfollowline, wwaiting, wturnright, wturnleft")


    # Starts loop then prompts user for input then goes to sleep until next command is entered
    while True:

        userin = raw_input()

        if userin == "stop":
            print ("stopping")
            gpg.stop()

        elif userin == "wfollowline":
            print("follow line")
            wrapper.followline()
            
        elif userin == "wstraight":
            wrapper.go_straight()
            
        elif userin == "wturnright":
            wrapper.turn_right()
            
        elif userin == "wturnleft":
            wrapper.turn_left()
            
        elif userin == "wwaiting":
            print("waiting status:")
            print(wrapper.waiting())

        elif userin == "straight":
            go_straight()

        elif userin == "turnaround":
            turn_around()

        elif userin == "turnright":
            print("right turn")
            ls.turn_right()

        elif userin == "turnleft":
            print("left turn")
            ls.turn_left()

        elif userin == "rp":
            print"READING POSITION"
            print(ls.read_position())

        elif userin == "rotations":
            print("The left wheel has gone: ")
            print(enc_read(0))
            print("The right wheel has gone: ")
            print(enc_read(1))

        elif userin == "read":
            print("READING")
            print(ls.read())

        elif userin == "followline":
            ls.follow_line()

        elif userin == "status":
            print("Current battery voltage:")
            print(volt())
            print(gpg.volt())


        elif userin == "speed":
            print(read_motor_speed());

        elif userin == "exit":
            print("Exiting\n")
            sys.exit()
            break

        time.sleep(.1)

if __name__ == '__main__':
    Main()

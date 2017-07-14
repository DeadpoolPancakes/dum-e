# uArm Swift Pro - Python Library Created by: Richard Garsthagen - the.anykey@gmail.com
#Waving python script

import uArmRobot
import time

serialport = "/dev/ttyACM0"  # for linux like system

# Connect to uArm 
myRobot = uArmRobot.robot(serialport)
myRobot.debug = False   # Enable / Disable debug output on screen, by default disabled
myRobot.connect()
myRobot.mode(0)   # Set mode to Normal

time.sleep(1)
myRobot.goto(200,0,100,6000)
myRobot.gripper(True)
time.sleep(5)
myRobot.goto(0,0,0,3000)
myRobot.gripper(False)
time.sleep(2)

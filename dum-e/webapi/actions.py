import uArmRobot
import time
import sys


def wave(self):
    myRobot.goto(200,0,100,6000)
    myRobot.gotorel(0,50,0,3000)
    myRobot.gotorel(0,-100,0,3000)
    myRobot.gotorel(0,100,0,3000)
    myRobot.gotorel(0,-100,0,3000)
    myRobot.goto(200,0,100,6000)

def nod(self):
    myRobot.goto(200,0,100,6000)
    myRobot.gotorel(50,0,0,3000)
    myRobot.gotorel(-100,0,0,3000)
    myRobot.gotorel(100,0,0,3000)
    myRobot.gotorel(-100,0,0,3000)
    myRobot.goto(200,0,100,6000)
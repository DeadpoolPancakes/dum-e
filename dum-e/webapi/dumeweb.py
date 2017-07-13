#!/usr/bin/env python
import uArmRobot
import time
import pantilthat
from sys import exit

serialport = "/dev/ttyACM0"  # for linux like system
myRobot = uArmRobot.robot(serialport)

try:
    from flask import Flask, render_template
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")


myRobot.debug = False   # Enable / Disable debug output on screen, by default disabled
myRobot.connect()
myRobot.mode(0)   # Set mode to Normal
app = Flask(__name__)
speed = 3000

time.sleep(1)
myRobot.goto(200,0,100,6000)

@app.route('/')
def home():
    return render_template('gui.html')

@app.route('/api/action/<action>')
def action(action)
    if action = "grip"
        myRobot.gripper(True)
        return "holding"
    
@app.route('/api/gripper/<int:on>')
def gripper(on):
    if on == 1:
        myRobot.gripper(True)
        return "on"
    elif on == 0:
        myRobot.gripper(False)
        return "off"    


@app.route('/api/pump/<int:on>')
def pump(on):
    if on == 1:
        myRobot.pump(True)
        return "on"
    elif on == 0:
        myRobot.pump(False)
        return "off"    

@app.route('/api/<direction>/<int:angle>')
def direction(direction, angle):
    if angle < 0 or angle > 180:
        return "{'error':'out of range'}"

    angle -= 90

    if direction == 'left':
        myRobot.gotorel(0,angle,0,speed)
        #return "{{'moving':{}}}".format(angle)
        return "moving left"

    elif direction == 'right':
        myRobot.gotorel(0,-angle,0,speed)
        #return "{{'moving':{}}}".format(angle)
        return "moving right"

    elif direction == 'up':
        myRobot.gotorel(0,0,angle,speed)
        #return "{{'moving':{}}}".format(angle)
        return "moving up"

    elif direction == 'down':
        myRobot.gotorel(0,0,-angle,speed)
       #return "{{'moving':{}}}".format(angle)
        return "moving down"

    elif direction == 'forward':
        myRobot.gotorel(angle,0,0,speed)
       #return "{{'moving':{}}}".format(angle)
        return "moving forward"

    elif direction == 'back':
        myRobot.gotorel(-angle,0,0,speed)
        #return "{{'moving':{}}}".format(angle)  
        return "moving back"      

    return "{'error':'invalid direction'}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9595, debug=True)

#!/usr/bin/env python
import uArmRobot
import time
import sys
from sys import exit

serialport = "/dev/ttyACM0"  # for linux like system
myRobot = uArmRobot.robot(serialport)

try:
    from flask import Flask, render_template
except ImportError:
    exit("This script requires the flask module\nInstall with: sudo pip install flask")

myRobot.debug = False   # Enable / Disable debug output on screen, by default disabled
myRobot.mode(0)   # Set mode to Normal
app = Flask(__name__)
speed = 3000
myRobot.connect()

@app.route('/')
def home():
    return render_template('gui.html')

@app.route('/api/connect/<int:connect>')
def connect(connect):
    if connect == 1:
        myRobot.connect()
        time.sleep(1)
        myRobot.goto(200,0,100,3000)
        return "{'dume':'connected'}"

    elif connect == 0:
        time.sleep(1)
        myRobot.end()
        return "{'dume':'disconnected'}"

@app.route('/api/buzzer/<int:time>/<int:frequency>')
def buzzer(time, frequency):
    myRobot.buzzer(frequency, time);

@app.route('/api/action/<action>')
def action(action):
    if action == 'grip':
        myRobot.gripper(True)
        return "{'dum-e':'holding'}"

    if action == 'suction':
        myRobot.pump(True)
        return "{'dum-e':'pump on'}"
    
@app.route('/api/gripper/<int:on>')
def gripper(on):
    if on == 1:
        myRobot.gripper(True)
        return "{'dum-e':'holding'}"
    elif on == 0:
        myRobot.gripper(False)
        return "{'dum-e':'letting go'}" 

@app.route('/api/pump/<int:on>')
def pump(on):
    if on == 1:
        myRobot.pump(True)
        return "{'dum-e':'pump on'}"
    elif on == 0:
        myRobot.pump(False)
        return "{'dum-e':'pump off'}"   

@app.route('/api/<direction>/<int:angle>')
def direction(direction, angle):
    
    if direction == 'left':
        myRobot.gotorel(0,angle,0,speed)
        return "{'dum-e':'moving left'}"

    elif direction == 'right':
        myRobot.gotorel(0,-angle,0,speed)
        return "{'dum-e':'moving right'}"

    elif direction == 'up':
        myRobot.gotorel(0,0,angle,speed)
        return "{'dum-e':'moving up'}"

    elif direction == 'down':
        myRobot.gotorel(0,0,-angle,speed)
        return "{'dum-e':'moving down'}"

    elif direction == 'forward':
        myRobot.gotorel(angle,0,0,speed)
        return "{'dum-e':'moving forward'}"

    elif direction == 'back':
        myRobot.gotorel(-angle,0,0,speed)
        return "{'dum-e':'moving back'}"      

    return "{'error':'invalid direction'}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9595, debug=True)

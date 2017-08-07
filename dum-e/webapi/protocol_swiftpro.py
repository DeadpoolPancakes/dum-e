# uArm Swift Pro - Python Library - protocol commands
# Created by: Richard Garsthagen - the.anykey@gmail.com
# V0.1 - June 2017 - Still under development
# v.05 august 2017 - deadpoolpancakes

## PROTOCOL MESSAGE
READY                   = "@1"
OK                      = "OK"
SET_POSITION            = "G0 X{} Y{} Z{} F{}"
SET_POSITION_RELATIVE   = "G2204 X{} Y{} Z{} F{}"
SET_POSITION_LASER      = "G1 X{} Y{} Z{} F{}"
SIMULATION              = "M2222 X{} Y{} Z{} P0"
GET_FIRMWARE_VERSION    = "P2203"
GET_HARDWARE_VERSION    = "P2202"
SET_ANGLE               = "G2202 N{} V{}"
SET_MODE                = "M2400 S{}"

# SET_RAW_ANGLE           = "sSerN{}V{}"
STOP_MOVING             = "G2203"
SET_PUMP                = "M2231 V{}"
GET_PUMP                = "P2231"
SET_GRIPPER             = "M2232 V{}"
GET_GRIPPER             = "P2232"
ATTACH_SERVO            = "M2201 N{}"
DETACH_SERVO            = "M2202 N{}"
GET_COOR                = "P2220"
GET_ANGLE               = "P2200"
GET_ANGLE_OF_JOINT      = "P2206 N{}"
# GET_RAW_ANGLE           = "gSer"
GET_IS_MOVE             = "M2200"
GET_TIP_SENSOR          = "P2233"
SET_BUZZER              = "M2210 F{} T{}"
SET_POLAR               = "G2201 S{} R{} H{} F{}"
GET_POLAR               = "P2221"
GET_EEPROM              = "M2211 N0 A{} T{}"
SET_EEPROM              = "M2212 N0 A{} T{} V{}"
GET_ANALOG              = "P2241 N{}"
GET_DIGITAL             = "P2240 N{}"
SET_BT                  = "M2234 V{}"

# grove modules
SET_GROVE               = "M2300 N{}"
GET_COLOR               = "M2301 N10 V{}"
#@10 N10 R20 G10 B255\n
GET_GESTURE             = "M2301 N11 V{}"
#@10 N11 V16\n (1: right; 2: left; 4: up; 8: down; 16: forward; 32: backward; 64: CW; 128: CCW;)
GET_ULTRASONIC          = "M2303 N12 V{}"
#@10 N12 V27\n
GET_TEMP                = "M2303 N15 V{}"
#@10 N15 T32.12 H76.5\n
GET_MOTION              = "M2303 N16 V{}"
#@10 N16 V1\n
SET_FAN                 = "M2303 N13 V{}"
# fan speed 0 - 255
SET_MAGNET              = "M2302 N14 V{}"

##LCD DISPLAY
SET_DISPLAY             = "M2303 N17 T{}"
SET_DISPLAY_RGB         = "M2303 N17 R{} G{} B{}"
SET_DISPLAY_TEXT        = "M2303 S{} V{}"
#S IS LINE AND V IS TEXT TO DISPLAY

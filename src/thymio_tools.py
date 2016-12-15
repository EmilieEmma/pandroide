# -*- coding: utf-8 -*-
from ThymioFunctions import *
from math import pi
import time
import random

speed = 50
angle_max = 90


def go_forward():
    setMotorSpeed(speed,speed)
    
def go_backward():
    setMotorSpeed(-speed,-speed)
    
def turn_left(angle):
    # computation to do with time
    time.sleep(angle*0.01)
    turn(angle)
    
def turn_right(angle):
    # computation to do with time
    time.sleep(angle*0.01)
    turn(-angle)
    
def front_detect():
    for capt in range(0,7):
        #print getSensorValue(capt)
        if getSensorValue(capt)!=0:
            return True
    return False

def good_noise():
    setSound(500,1)

def bad_noise():
    setSound(200,1)

def stop():
    setMotorSpeed(0,0)
    
def random_walk():
    # random action launched
    action = random.randint(1, 8)
    print "-> Action =",action
    # Go forward
    if action%2 == 0 :
        go_forward()
        sleepTime = random.randint(1,3)
        print "\tStreet ahead ({} sec)".format(sleepTime)
        time.sleep(sleepTime)
    # Turn Left
    elif action == 1 :
        print "\tTurning left"
        turn_left(random.randint(1,angle_max))
    # Turn Right
    elif action == 3 :
        print "\tTurning right"
        turn_right(random.randint(1,angle_max))
    # Go backward
    elif action == 5 :
        go_backward()
        sleepTime = random.randint(1,3)
        print "\tBackward ({} sec)".format(sleepTime)
        time.sleep(sleepTime)
    # Stop
    elif action == 7 :
        print "\tPaused (1sec)"
        stop()
        time.sleep(1)
    # if there is some obstacles in front of the robot -> turn left
    """
    if front_detect():
        print "Truc devant"
        turn_left(random.randint(0,angle_max))
	"""

"""
i=0
while i<100:
    i+=1
    print "it :",i
    if front_detect():
        print "Truc devant"
        turn_left(random.randint(0,angle_max))
"""
# To avoid conflicts between gobject and python threads
"""import gobject
gobject.threads_init()
dbus.mainloop.glib.threads_init()
"""
#print in the terminal the name of each Aseba NOde
#print network.GetNodesList()  
#GObject loop
#print 'starting loop'
"""
loop = gobject.MainLoop()
loop.quit()
context = loop.get_context()
i = 0
while i<10:
    try:
        handle = gobject.timeout_add(100, good_noise)  # every 0.1 sec
        time.sleep(3)
    except KeyboardInterrupt:
        handle = gobject.timeout_add(100, bad_noise)  # every 0.1 sec
    if context.pending():
        context.iteration()
    else:
        time.sleep(2)
    i+=1

loop.quit()

try:
    #call the callback of Braitenberg algorithm
    handle = gobject.timeout_add (1000, good_noise) #every 0.1 sec
    loop.run()
except KeyboardInterrupt :
    loop.quit()
    time.sleep(1)
    try:
        handle = gobject.timeout_add(100, bad_noise)  # every 0.1 sec
        loop.run()
    except KeyboardInterrupt:
        loop.quit()
"""

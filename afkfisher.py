####Alexander Black, Minecraft AFK Fisher
##Settings
refreshwait = .25
blurdegree = 15


##Imports
import pyautogui; import cv2; import numpy as np; import time

##Information prints
print( "Welcome! This script is designed to run on the primary display as fullscreen. \n\
Ensure you are directly above the water, crouch-walk distance from platform to hover.\n\
Remember to look straight down, and have the rod extended prior to executing this code \n\
A hopper underneath the water is ideal, though you must be out of clicking distance.\n\
Finally, ensure you are completly surrounded by dark colors, as this code looks for the white of the bobber." )

##Actual code
time.sleep( 5 )
i = 0
while True:
    pre = pyautogui.screenshot()                                                #Grab screencapture
    img = cv2.cvtColor( np.array( pre ), cv2.COLOR_BGR2GRAY )                   #Convert to OpenCV (numpy array)
    w, h = img.shape                                                            #Get dimensions (width & height)
    img = img[ int( w / 4 ):int( 3 * w / 4 ), int( h / 4 ):int( 3 * h / 4 ) ]   #Numpy slicing to crop center area
    img = cv2.blur( img, ( blurdegree, blurdegree ) )                           #Blurs code to remove small images (ex. crosshair)
    img = cv2.inRange( img, np.array( [ 180 ] ), np.array( [ 255 ] ) )          #Finds the white of the bobber
    if not np.array( [ 255 ] ) in img:                                          #Detects lack of bobber
        i += 1
        pyautogui.click( button = 'right' )                                     #Retract bobber
        time.sleep( .5 )
        pyautogui.click( button = 'right' )                                     #Extend bobber
        time.sleep( 1.5 )
        print( i )                                                              #Times extended
    time.sleep( refreshwait )

import xbmc, xbmcgui
import sys
import os
import time
import socket
from socket import timeout


print "starting client"
root  = os.path.dirname(__file__)


#BUILD THE ADDON GRAPHICS
win = xbmcgui.Window(10000)
#LEAP Main icon
leapLogo = xbmcgui.ControlImage(150,10,155,75, root + '/image/leapLogo.png')
win.addControl(leapLogo)


#hand icons
leftHand = xbmcgui.ControlImage(303,10,45,45, root + '/image/leftHandIcon.png')
print leftHand.getId()
win.addControl(leftHand)
#print win.getControl(0)


rightHand = xbmcgui.ControlImage(366,10,45,45, root + '/image/rightHandIcon.png')
print rightHand.getId()
win.addControl(rightHand)


#mode Labels
global modeLabel
modeLabel = xbmcgui.ControlLabel(430, 15, 200, 90, '', 'font14', '0xFFFFFFFF')
modeLabel.setLabel('Navigation')
#print modeLabel.getId()
win.addControl(modeLabel)




#blocking simple server-blocking in order to clean up if connection expires.
host = socket.gethostname()
port = 50000
backlog = 5 
size = 1024 
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket.bind((host,port)) 
socket.listen(backlog)
#socket.settimeout(60) 

socketFlag = True
try:
    connection, address = socket.accept()
except timeout:
    print "waiting connection timed out"
    socketFlag = False

while socketFlag:        
    try:
        data = connection.recv(1024)    
        #Do things
        #possibly implement this as json handler at some point
        print data

        if data == "ruok":
            print "imok"
            xbmcgui.Dialog().ok("Dev", "imok")

       
        if data == "PlaybackMode": 
            print "Playback Mode"
            
            #win.removeControl(modeLabel)
            #modeLabel = xbmcgui.ControlLabel(430, 15, 200, 90, '', 'font14', '0xFFFFFFFF')
            modeLabel.setLabel('Playback Mode')
            #win.addControl(modeLabel)

        if data == "NavigationMode": 
            print "Navigation Mode"
          
            #win.removeControl(modeLabel)
            #win.get
            #modeLabel = xbmcgui.ControlLabel(430, 15, 200, 90, '', 'font14', '0xFFFFFFFF')
            modeLabel.setLabel('Navigation Mode')
            #win.addControl(modeLabel)







    except timeout:
        print "waiting connection timed out"
        break

    if data == "close":
        print "stopping"             
        break

    if not data:
        print 'Connection lost. Listening for a new controller.' 
        break

#end of simple server



print "cleaning up and closing"





win.removeControl(leapLogo)
win.removeControl(leftHand)
win.removeControl(rightHand)
win.removeControl(modeLabel)








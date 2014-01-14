import socket
import Leap
import time

from Leap import SwipeGesture



s = ""
lastX = 0
#while True:
#	mydata = raw_input('Prompt :')
#	print (mydata)
#	if mydata=="g":
#		s.send( '{"jsonrpc": "2.0", "id": 1, "method": "Input.Left"}' )
#	elif mydata=="h":
#		s.send( '{"jsonrpc": "2.0", "id": 1, "method": "Input.Right"}' )
#	elif mydata=="x":
#		break
class SampleListener(Leap.Listener):


    def on_connect(self, controller):
        print "\nConnected"

        # Enable gestures
        #controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        #controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        #controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

        if(controller.config.set("Gesture.Swipe.MinLength", 0.0) 
            and controller.config.set("Gesture.Swipe.MinVelocity", 0)):
            controller.config.save()
       
       

    def on_frame(self, controller):
        global lastX
        global s
        #global handDirection

        
        #x=0

        frame = controller.frame()
      
            #pastFrame = frame.id - 50
        hand = frame.hands[0]
       
        

        if hand.id > 0 and hand.palm_position.y < 100:
            global lastX
            global s
            #print hand
            #print frame.id
            #print hand.stabilized_palm_position, hand.palm_velocity
            #print hand.palm_position.x
            #print abs(lastX - hand.palm_position.x)
            #print lastX
            x = hand.palm_position.x

            if lastX == 0:
                lastX = x
            else:
                if  x < 0: 

                    print x, lastX, "swipe left"
                    s.send( '{"jsonrpc": "2.0", "id": 1, "method": "Input.Left"}' )
                    time.sleep(1)

                elif x > 0:
                    print x, lastX, "swipe right"
                    s.send( '{"jsonrpc": "2.0", "id": 1, "method": "Input.Right"}' )
                    time.sleep(1)
                lastX = 0

        #else: 
            #lastX = 0
            #print frame.id



            #lastX = xPosition

            
           
                
                
                                

        #gesture = frame.gestures()[0]
        #    global myGest
        #    myGest = gesture
        #    break

        #gestId = myGestureList.id
        #print len(myGestureList)
        #gestId = myGestureList

        #if gesture.type == Leap.Gesture.TYPE_SWIPE:
        #    swipe = SwipeGesture(gesture)
        #    gestId = gesture.id
        #    gestPosition = swipe.position
        #    gestDirection = swipe.direction
        #    gestSpeed = swipe.speed
        
        #    if x + 3 < gestId and hand.palm_position.y < 100:
        #        print  gestId,gestPosition, gestDirection, gestSpeed
        #        if gestDirection.x < 0:
        #            s.send( '{"jsonrpc": "2.0", "id": 1, "method": "Input.Left"}' )
        #        elif gestDirection.x > 0:
        #            s.send( '{"jsonrpc": "2.0", "id": 1, "method": "Input.Right"}' )
        #        x = gestId



            #x = x + 1
        #print "Swipe id: %d, position: %s, direction: %s, speed: %f" % ()
                
                
        #print pastFrame
        #handChange = hand.translation(pastFrame).x 

        #if  handChange < 0 and hand.palm_position.y < 200:
        #    print "left", handChange , " " , hand.palm_position.y
        #elif handChange > 0 and hand.palm_position.y < 200:
        #    print "right", handChange, " ",  hand.palm_position.y


        #elif x ==20:
         #   
          #  handDirection=0


        #x = x + 1
        #print x
def xmbcConnect():
    global s
    s = socket.socket()
    host = socket.gethostname()
    port = 9090
    s.connect((host,port))


def main():

    xmbcConnect()
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    mydata = raw_input('Press any key to quit')
    #print (mydata)

    # Remove the sample listener when done
    controller.remove_listener(listener)
    s.close()

if __name__ == "__main__":
    main()
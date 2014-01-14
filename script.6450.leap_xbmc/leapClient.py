
#to do implement json calls for playback mode
#implement guard for entering playback mode-line 122

import Leap, socket, time 
from operator import le
import numpy


#touchPointListener extends Leap.Listener 
class TouchPointListener(Leap.Listener):

    #brought in from Leap.Listener parent, run one time when object is created
    def on_init(self, controller):
        print "Initialized"


       


        

        #control socket
        self.s = socket.socket()        
        host = socket.gethostname() #get localhost by default
        port = 9090
        self.s.connect((host,port))



        #gui socket
        self.guiSock = socket.socket()        
        host = socket.gethostname() #get localhost by default
        port = 50000
        self.guiSock.connect((host,port))

        




        #state variables for circle gesture
        self.circleActiveFlag = False
        #self.circlePastProgress = -1
        self.circleCount = 0



        #sets a two hand mode flag
        self.twoHandModeFlag = False
        self.twoHandTimeout = 0 


        #set if an flatHandAction is being performed
        self.flatHandFlag = False



        #setup timestamp comparison variables
        self.currentTime = 0
        self.previousTime = 0



        
        self.startVar = 0

        self.theList = []
        self.timeList = [] # Leap.Vector(0,0,0)
        self.veloList = [] #Leap.Vector(0,0,0)
        self.distList = [] #Leap.Vector(0,0,0)
        self.veloAvg = 0 
        self.x = 0
        self.pauseTest = 0
        self.frameIterator = 0


        self.playbackModeFlag = "Nav"
        
      



    def on_exit(self,controller):
     
        self.s.close()
        self.guiSock.close()

        
    #brought in from Leap.Listener parent, run one time when the code connects to the Leap Hardware device
    def on_connect(self, controller):
        print "Connected"

        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        #controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);    
        
        #circle gesture adjust
        if(controller.config.set("Gesture.Circle.MinRadius", 1.0) 
           and controller.config.set("Gesture.Circle.MinArc", .5*3.1415926535) ):
            controller.config.save()

        
       
    #brought in from parent class this is called EACH FRAME that the Leap hardware device runs
    #lots per second
    def on_frame(self, controller):   
             #if(controller.frame(60)  )
        self.frameIterator +=1



        #loads up all the frames before starting the program
        if( self.startVar < 60):
          self.startVar += 1
          return            
    
    

        #leap-the frame contains EVERYTHING leap related:
        # hands, fingers, pointables, interaction_box, and much more
        frame = controller.frame()
   

        # two hand detection logic
        #due to the sporadic noisy nature of the leap detection, instead of using polling
        #decided to use a registration system where motions/events register for a particular 
        #period of time
        #more robust and stable 

        """
        if ( len(frame.hands) >=2 ):
            if self.twoHandModeFlag == False:
                print "twoHandMode-ENGAGE"
            self.twoHandModeFlag = True
            self.twoHandTimeout = frame.timestamp
            self.guiSock.send("PlaybackMode")
            self.playbackModeFlag = "Play"


        if ( (frame.timestamp - self.twoHandTimeout) >= (3 * 1000000) ) and (self.twoHandModeFlag == True): 
            self.twoHandModeFlag = False
            print "twoHandMode-DIS-ENGAGE"
            self.guiSock.send("NavigationMode")
            self.playbackModeFlag = "Nav"
        """

        if ( (frame.timestamp - self.twoHandTimeout) >= (5 * 1000000) ): 
            self.twoHandModeFlag = True

        
        if ( len(frame.hands) >=2 and self.playbackModeFlag == "Nav" and self.twoHandModeFlag == True ):  
            print "twoHandMode-ENGAGE"
            #check to make sure only at main screen before entering Playback Mode!!
            #don't want to enter it in other windows.
            self.guiSock.send("PlaybackMode")
            self.playbackModeFlag = "Play"

            self.twoHandTimeout = frame.timestamp
            self.twoHandModeFlag = False

        if ( len(frame.hands) >= 2 and self.playbackModeFlag == "Play" and self.twoHandModeFlag == True): 
            print "twoHandMode-ENGAGE"
            self.guiSock.send("NavigationMode")
            self.playbackModeFlag = "Nav"

            self.twoHandTimeout = frame.timestamp
            self.twoHandModeFlag = False

        


        #FLAT HAND GESTURE
        self.flatHandFlag = False
        #flat hand gesture logic-only works in single hand mode
        if len(frame.pointables) >= 4 and frame.pointables.frontmost.tip_position.z > 0:
            self.flatHandFlag = True
            self.onFlatHandAction()            
            time.sleep(.5)




        
        #POINTERS
        #selection and navigation logic
        #single handed mode logic
        if len(frame.pointables) > 1:

        
            #frontmost = frame.pointables.frontmost          
            theFrontmost = frame.pointables.frontmost

            frontmost = theFrontmost.stabilized_tip_position 

            if(frontmost.x > -50 and frontmost.x < 50 and frontmost.z < 0):
                self.onCenterSelectAction()
            elif(frontmost.x < -50 and frontmost.z < 0):
                self.onLeftSelectAction()
            elif(frontmost.x > 50 and frontmost.z < 0):
               self.onRightSelectAction()
   
            """
            if(frontmost.tip_position.x > -50 and frontmost.tip_position.x < 50 and frontmost.tip_position.z < 0):
                self.onCenterSelectAction()
            elif(frontmost.tip_position.x < -50 and frontmost.tip_position.z < -50 and frontmost.tip_position.z < 0):
                self.onLeftSelectAction()
            elif(frontmost.tip_position.x > 50 and frontmost.tip_position.z < -50 and frontmost.tip_position.z < 0):
               self.onRightSelectAction()
            """
            time.sleep(.4)




        #nteractionBox = controller.frame().interaction_box

       

          
        #normalizedPosition = interactionBox.normalize_point(stabilizedPosition)
        #x = normalizedPosition.x * windowWidth
        #y = windowHeight - normalizedPosition.y * windowHeight
            











            

        
        frame = controller.frame()

        #GESTURES
        for gesture in frame.gestures():


            """
            #SWIPE
            if gesture.type == Leap.Gesture.TYPE_SWIPE:

                swipe = Leap.SwipeGesture(gesture)

                #if(this.gestureId != gesture.id):
                if swipe.state == 1:
                    if(swipe.direction.x > 0):
                        #print "swipe right \n" + "gesture id: " + str(gesture.id) 
                        self.onLeftSelectAction()
                    elif(swipe.direction.x < 0):
                        #print "swipe left\n" + "gesture id: " + str(gesture.id)
                        self.onLeftSelectAction()
            """



            
            #CIRCLE
            if gesture.type == Leap.Gesture.TYPE_CIRCLE and not self.flatHandFlag:

                PIEDAWG = 3.1415926535
               

                #determine clockwiseness
                circle = Leap.CircleGesture(gesture)
                if (circle.pointable.direction.angle_to( circle.normal ) <=  PIEDAWG/4 ):
                    clockwiseness = "clockwise"
                else:
                    clockwiseness = "counterclockwise"              
                




                #limits the range of where the circle can be activated(right on top of the leap)
                if circle.center.x > -50 and circle.center.x < 50 and circle.center.z > 0:

                    #this is the start of the circular motion
                    if circle.state == 1:                  
                        print "Circle Begin" + str(gesture.id)
                        #self.circleActiveFlag = True
                        self.circleCount = 0
                      


                    #this is the actual actions during the circular motion
                    if circle.state == 2:              
                        #pass

                        #self.circleCount = self.circleCount + 1;
                        if self.circleCount % 20  == 0:
                            #print "the trimmed trigger " + str(gesture.id)                        
                            if(clockwiseness == "clockwise"):
                                self.onClockwiseAction()
                            elif(clockwiseness=="counterclockwise"):
                                self.onCounterClockwiseAction() 
                        self.circleCount += 1
                            


                    #the action called during the termination of the circular motion
                    if circle.state == 3:
                        print "Circle Complete"
                        #self.circleActiveFlag = False
                        #self.circlePastProgress = 0

                        time.sleep(1)
                       
                       
                        


       
       


    


       
        

        
       

  
         

        
        
    




    def onFlatHandAction(self):
        print "onFlatHand"

        #if self.playbackModeFlag =="Nav":
        self.s.send( '{"jsonrpc": "2.0", "id": 1, "method": "Input.Back"}' )
        #elif self.playbackModeFlag =="Play":
        #    pass


    def onClockwiseAction(self):
        print "clockwise"
        #if self.playbackModeFlag == "Nav":
        self.s.send('{"jsonrpc": "2.0", "id": 1, "method": "Input.Down"}')
        #elif self.playbackModeFlag =="Play":
            #pass

    def onCounterClockwiseAction(self):
        print "counterclockwise"
        #if self.playbackModeFlag == "Nav":
        self.s.send('{"jsonrpc": "2.0", "id": 1, "method": "Input.Up"}')
        #elif self.playbackModeFlag =="Play":
            #pass
        
    def onLeftSelectAction(self):
        print "navigating left"

        #if self.playbackModeFlag == "Nav":
        self.s.send('{"jsonrpc": "2.0", "id": 1, "method": "Input.Left"}')
        #elif self.playbackModeFlag =="Play":
            #pass

    def onRightSelectAction(self):
        print "navigating right"
        #if self.playbackModeFlag == "Nav":
        self.s.send('{"jsonrpc": "2.0", "id": 1, "method": "Input.Right"}')
        #elif self.playbackModeFlag =="Play":
            #pass

    def onCenterSelectAction(self):
        print "frontmost < = 0.  Selection!!"

        #if self.playbackModeFlag == "Nav":
        self.s.send('{"jsonrpc": "2.0", "id": 1, "method": "Input.Select"}')
        #elif self.playbackModeFlag =="Play":
        #    pass

    def setTwoHandFlag(self):
        print "bothHands"
        ##self.s.send("leftHandOn")
        ##self.s.send("rightHandOn")
        #pass
    
  



def main():


        #control socket
        s = socket.socket()
        host = socket.gethostname() #get localhost by default
        port = 9090
        s.connect((host,port))
        #opens up the addon
        s.send('{"jsonrpc": "2.0", "id": 1, "method": "Addons.ExecuteAddon", "params":{"addonid":"script.6450.leap_xbmc" }} ')
        time.sleep(3)
        s.close()





        #leap-sets up the leap stuff
        leapController = Leap.Controller()
        leapController.set_policy_flags(Leap.Controller.POLICY_BACKGROUND_FRAMES)

        tpListener = TouchPointListener()

        leapController.add_listener(tpListener)


        mydata = raw_input('Press any key to quit')

        leapController.remove_listener(tpListener)
       





if __name__ == "__main__":
    main()
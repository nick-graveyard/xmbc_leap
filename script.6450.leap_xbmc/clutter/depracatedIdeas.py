"""
class changeImage(threading.Thread):
    def __init__(self):
        self.displayFlag =True
        threading.Thread.__init__(self)

    def run(self):

        while True:
            if self.displayFlag==True:
                win.removeControl(testA)
                self.displayFlag = False
            elif self.displayFlag == False:
                win.addControl(testA)
                self.displayFlag =True

            time.sleep(3)

theThread = changeImage()
theThread.start()
"""





ACTION_PREVIOUS_MENU = 10
ACTION_SELECT_ITEM = 7
ACTION_PARENT_DIR = 9

class TestWindowClass(xbmcgui.Window):
  def __init__(self):
    self.addControl(xbmcgui.ControlImage(0,0,250,250, '/leapLogo.png'))
    self.strActionInfo = xbmcgui.ControlLabel(100, 120, 200, 200, '', 'font13', '0xFFFF00FF')
    self.addControl(self.strActionInfo)
    self.strActionInfo.setLabel('Push BACK to quit, A to display text and B to erase it')
 
  def onAction(self, action):
    if action == ACTION_PREVIOUS_MENU:
      self.close()
    if action == ACTION_SELECT_ITEM:
      self.strAction = xbmcgui.ControlLabel(300, 200, 200, 200, '', 'font14', '0xFF00FF00')
      self.addControl(self.strAction)
      self.strAction.setLabel('Hello world')
    if action == ACTION_PARENT_DIR:
      self.removeControl(self.strAction)
 
mydisplay = TestWindowClass()
mydisplay .doModal()
del mydisplay
#print "starting addon"



 """
        #if len(frame.pointables) == 0 and self.pointablesFlag == "yesPointables":
        #    self.onClenchAction()
        #    self.pointablesFlag = "noPointables"
        #print "---NEW----"
        lengthFlag = True

        for pointable in frame.pointables:
            if pointable.length > .2:
                lengthFlag = False
                


        if lengthFlag and self.pointablesFlag == "yesPointables":

            for pointable in frame.pointables:
                print str(pointable.length)


            self.onClenchAction()
            self.pointablesFlag = "noPointables"


        
            print "length: " + str(pointable.length)
             + "number:" + str(i)
            i = i + 1
        
        """

       

        """
        #HANDS   
        if (numHands == 0) and (self.handFlag != "noHands"):
            self.onNoHandsAction()
            self.handFlag = "noHands"
          
        if (numHands == 1)  and (self.handFlag != "oneHands"):
            self.onOneHandAction()
            self.handFlag = "oneHands"
           
        if (numHands == 2) and (self.handFlag != "twoHands"):
            self.onBothHandAction()
            self.handFlag = "twoHands"
        
        """
        
        #print "normalizedHandNumber: " + str(normalizedHandNumber)
        

        def regPause(self, inCurrentTime, inName):
        self.pauseList.

    def testPause(self, inCurrentTime, inName):
            if item[inName] 
                return False
            else:
                return True 




        #this is frameCache info.
        #set the frameCache with this variable. - this normalizes the data over a range
        #smoothes it out but also adds a slight delay to any changes.
        self.cacheSize = 200
        self.frameCache = [-1] * self.cacheSize
        self.frameIter = 0
        #adds frames to frame cache as they become available
        #note: the built in controller.frame(some number) history only can handle a history of 60!!
        #so created a frame cache to hande more
        self.frameCache[self.frameIter] = frame
        self.frameIter = (self.frameIter + 1) % self.cacheSize

        #normHandNum->gets the normalized hand number over the entire frame cache
        normalizedHandNumber = 0 
        normalizedPointerNumber = 0       
        for myIter in self.frameCache:
            if myIter is -1:
               break
            else:
                #put all frame cache actions here in this iterator
                normalizedHandNumber = max(normalizedHandNumber, len(myIter.hands) ) 
                normalizedPointerNumber = max(normalizedPointerNumber, len(myIter.pointables) )
                pass

        #print "norm hands: " + str(normalizedHandNumber) + "norm pointables: " + str(normalizedPointerNumber)


    def calcTimeDiff(self, startTime, endTime, max):
        if time1 > time2:
            return (max - time1) + time2
        else:
            return (time2 - time 1)



             

        print frame.timestamp - self.twoHandTimeout
        print (frame.timestamp - self.twoHandTimeout) >= (5 * 100000) 
        print "twohand flag " + str(self.twoHandFlag)
           

              print len(frame.hands)

           #print "circle trigger " + str(gesture.id)
                        
                        #original way to implement circle prgress before finding out about 
                        #the circle progress variable
                        self.circleCount = self.circleCount + 1;
                        if self.circleCount % 5  == 0:
                            pass
                            #print "the trimmed trigger " + str(gesture.id)                            
                      




                       #captures the changes of the circle progress variable by comparing it to a past state
                        if self.circlePastProgress != round(circle.progress):
                            if(clockwiseness == "clockwise"):
                                self.onClockwiseAction()
                                print "circle.progress: " + str( round(circle.progress) )
                            elif(clockwiseness=="counterclockwise"):
                                self.onCounterClockwiseAction()
                                print "circle.progress: " + str( round(circle.progress) )
                        self.circlePastProgress = round(circle.progress)






        #navigation mode
        if self.NavigationMode == 0:
            if data == "up":
                return_json = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Input.Up"}')
            if data == "down":
                return_json = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Input.Down"}')
            if data == "left":
                return_json = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Input.Left"}')
            if data == "right":
                return_json = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Input.Right"}')
            if data == "back":
                return_json = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Input.Back"}')
            if data == "select":
                return_json = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Input.Select"}')

        #playback mode
        elif self.NavigationMode == 1:

            #activePlayers = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Player.GetActivePlayers"}')
            #return is in this format{"id":1,"jsonrpc":"2.0","result":[{"playerid":0,"type":"audio"}]}
            #print activePlayers
            """
            if data == "up":
                return_json = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Input.Up"}')
            if data == "down":
                return_json = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Input.Down"}')
            if data == "back":
                return_json = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "id": 1, "method": "Input.Back"}')
            """
            if data == "right":
                return_json = xbmc.executeJSONRPC('{"jsonrpc":"2.0","id":1, "method":"Player.GoTo","params":{"playerid":0,"to":"next"}}')
            if data == "left":
                return_json = xbmc.executeJSONRPC('{"jsonrpc":"2.0","id":1,"method":"Player.GoTo","params":{"playerid":0,"to":"previous"}}')
            if data == "select":
                return_json = xbmc.executeJSONRPC('{"jsonrpc":"2.0","id":1,"method":"Player.PlayPause","params":{"playerid":0}}')



        #general commands that will work in any mode

        #these are for toggling the hand presence icons from white to green
        if (data =="rightHandOn") and (self.rightOn == False):
            self.win.removeControl(self.rightHandEmpty)
            self.win.addControl(self.rightHandPresent)
            self.rightOn = True
        if (data =="leftHandOn") and (self.leftOn == False):
            self.win.removeControl(self.leftHandEmpty)
            self.win.addControl(self.leftHandPresent)
            self.leftOn = True
        if (data =="rightHandOff") and (self.rightOn == True):
            self.win.addControl(self.rightHandEmpty)
            self.win.removeControl(self.rightHandPresent)
            self.rightOn = False
        if (data =="leftHandOff") and (self.leftOn == True):
            self.win.addControl(self.leftHandEmpty)
            self.win.removeControl(self.leftHandPresent)
            self.leftOn = False

        #toggles the mode variable through the list of modes
        if data == "modeToggle":
            listLen = len(self.NavigationList)
            self.NavigationMode = (self.NavigationMode + 1) % listLen
            self.modeLabel.setLabel( self.NavigationList[self.NavigationMode] )
            print self.modeLabel.getLabel()





                #handle duration time of gesture
                self.timeList.append(frame(0).timestamp - frame(1).timestamp)

                #handle distance traveled of gesture-vector
                self.distList.append( frame(0).pointable(thePernta).tip_position - frame(1).pointable(thePernta).tip_position )

                #handle velocity changes
                self.veloList.append( frame(0).pointable(thePernta).tip_position - frame(1).pointable(thePernta).tip_position  )

                
                print "woekrinasdf " + str(frontmost.direction)

                #for vector in self.distList:
                #    vector.x



            else:
                """
                if ( ( sum(timeList)/len(timeList) )  > timeTrigger ) and ( (sum(distList)/len(distList) ) > distTrigger ):
                    pass

                else:
                    distList  = []
                    veloList = []
                    timeList = []
                """
                pass

                

### SWIPE IMPLEMENTING
 velocity = controller.frame(0).pointables.frontmost.tip_velocity.x
        velocityLast = controller.frame(1).pointables.frontmost.tip_velocity.x
        velocityLastLast = controller.frame(2).pointables.frontmost.tip_velocity.x

        if self.frameIterator % 3 == 0 and controller.frame(0).pointables.frontmost.tip_velocity.x > 5:

            print "the velocitys"
            print velocity
            self.theList.append(velocity)
            print velocityLast
            self.theList.append(velocityLast)
            print velocityLastLast
            self.theList.append(velocityLastLast)
            print "the deviations"
            print numpy.std(self.theList)
            print "the sum"
            print sum(self.theList)



            position1 = controller.frame(0).pointables.frontmost.tip_position.x
            print "pos 1:" +  str(position1)
            positionLast = controller.frame(1).pointables.frontmost.tip_position.x
            print "pos 2:" + str(positionLast)
            positionLastLast = controller.frame(2).pointables.frontmost.tip_position.x
            print "pos 2:" + str(positionLast)

            del self.theList[:]
            #time.sleep(.5)





            """
            velocity = 0 
            norm = 0
            theList = []
            for i in range(0,5):
                velocity = controller.frame(i).pointables.frontmost.tip_velocity.x
                theList.append(velocity)
                #print controller.frame(i).pointables.frontmost.tip_velocity.x
           
               

            numVariance = numpy.var(self.theList)
            numMean = sum(self.theList)/len(self.theList)
            #print numMean

           


            if (numMean > 0):
                self.onRightSelectAction()
            elif (numMean < 0):
                self.onLeftSelectAction()
        


            if(numMean > 1):
                print "var:" + str(numVariance)
                print "mean:" + str(numMean)
                print "velocity: " + str(numMean)
                print "/n"

            #time.sleep(.5)




            """
            

        ##_------





        





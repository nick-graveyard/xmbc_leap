import xbmc, xbmcgui
import os

class DataHandler(object):

    def __init__(self):
        root  = os.path.dirname(__file__)
        self.win = xbmcgui.Window(10000)
        

        #create/add base icons

        

        

        
        

        #setup for hand state icons
        self.leftHandPresent= xbmcgui.ControlImage(303,10,45,45, root + '/image/leftHandIconGo.png')
        self.rightHandPresent = xbmcgui.ControlImage(366,10,45,45, root + '/image/rightHandIconGo.png')

        #flags for hand state protections
        self.leftOn = False
        self.rightOn = False

        #sets the navigation mode state
        #add to navigation list as needed (dont change navigation mode, it's just an initializer)
        #The navigation mode is changed in the modeToggle section
        self.NavigationList =["Navigation", "Playback"]
        self.NavigationMode = 0


    #SERVER SIDE EVENT HANDLER
    def handle(self,data):       
        print data
     

        #dev testing
       

        #this kills the entire addon
        if data == "close":
            xbmcgui.Dialog().ok("Leap Xmbc Addon","Stopped") 
            sys.exit(0)

        else:
            pass
            #xbmc.executeJSONRPC(data)

from Tkinter import Tk,mainloop, Frame, Canvas
import Leap, tkFont, socket


#touchPointListener extends Leap.Listener 
class TouchPointListener(Leap.Listener):

    #brought in from Leap.Listener parent, run one time when object is created
    def on_init(this, controller):
        print "Initialized"

        this.xmbcConnect();

        
    #brought in from Leap.Listener parent, run one time when the code connects to the Leap Hardware device
    def on_connect(this, controller):
        print "Connected"

        #this is required to enable the SWIPE gesture 
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

        #these are initializing some instance variables for gesture functionality
        this.x = 0
        this.gestureId = 0
        this.theText = "no gesture detected"


        #tune these two parameters to make the swipe gesture more or less sensitive
        swipe_length = 100.0
        swipe_velocity = 750

        #sets the actual swipe config in the Leap.
        if(controller.config.set("Gesture.Swipe.MinLength", swipe_length)
          and controller.config.set("Gesture.Swipe.MinVelocity", swipe_velocity)):
            controller.config.save()

        #if you keep your console open you get some good messages while the program is running
        print "swipe length: " + str( controller.config.get("Gesture.Swipe.MinLength")   )
        print "swipe velocity: " + str( controller.config.get("Gesture.Swipe.MinVelocity") )
        

       

       
    #brougt in from parent class this is called EACH FRAME that the Leap hardware device runs
    #lots per second
    def on_frame(this, controller):

        #tkinter-clear the canvas each frame
        this.paintCanvas.delete("all")


        #leap-the frame contains EVERYTHING leap related:
        # hands, fingers, pointables, interaction_box, and much more
        frame = controller.frame()


        #create an leap interaction box- this is for 2d touch emulation by providing a simple z coordinate
        #https://developer.leapmotion.com/documentation/Languages/Python/Guides/Leap_Touch_Emulation.html
        this.interactionBox = frame.interaction_box


        #draw interaction box(calls the local function)
        this.paint_interaction_box()

        #draw gesture indicator(in the center of the screen telling gesture direction/id)
        tempfont = tkFont.Font(family='Helvetica', size=int(20) ) 
        this.gestureIndicator = this.paintCanvas.create_text(640,400, text=this.theText, font=tempfont)



        #prints gesture information to both the console and the screen
        if(len( frame.gestures() ) > 0):
           
            gestureList = frame.gestures()
            gesture = gestureList[0]
            
            this.x = this.x + 1
            print str(this.x)
            swipe = Leap.SwipeGesture(gesture)
            print "Swipe id: %d, position: %s, direction: %s, speed: %f" % (
                            gesture.id, swipe.position, swipe.direction, swipe.speed)

            if(this.gestureId != gesture.id):
                if(swipe.direction.x > 0):
                    this.theText = "swipe right \n" + "gesture id: " + str(gesture.id) 
                    this.s.send( '{"jsonrpc": "2.0", "id": 1, "method": "Input.Right"}' )

                elif(swipe.direction.x < 0):
                    this.theText =  "swipe left\n" + "gesture id: " + str(gesture.id)
                    this.s.send( '{"jsonrpc": "2.0", "id": 1, "method": "Input.Left"}' )

              

            
            #updates the gesture Id each time this function is called.
            this.gestureId = gesture.id




   

    
       
            #iterates through each pointer(i.e. finger) visible in the frame
        for pointable in frame.pointables:

            #stabilized_tip_position: removes jitter and makes the position more stable
            #normalize_point: converts the coordinate to 0-1 scale to allow for percentage scaling
            normalizedPosition = this.interactionBox.normalize_point(pointable.stabilized_tip_position)
          

            #changes the frontmost color to red and sets the rear pointers to blue
            if(pointable == frame.pointables.frontmost):
                color = this.rgb_to_hex((200,0,0))
            else:
                color = this.rgb_to_hex((0,0,200))

            #draw the pointers(by calling the draw function)
            this.draw(normalizedPosition.x * 1280, 800 - normalizedPosition.y * 800, normalizedPosition.z * 1, normalizedPosition.z * 300, normalizedPosition.z * 300, color)



            #not sure whats going on here-artifact from program on leap website
            #kept because it contains some juicy stuff might possibly be interested in
            """
            if(pointable.touch_distance > 0):
                color = this.rgb_to_hex((0, 255 - 255 * pointable.touch_distance, 0))

            elif(pointable.touch_distance <= 0):
                color = this.rgb_to_hex((-255 * pointable.touch_distance, 0, 0))
                #color = this.rgb_to_hex((255,0,0))

            else:
           
            if(pointable.touch_zone == Leap.Pointable.TOUCHING):
                this.draw(normalizedPosition.x * 1280, 800 - normalizedPosition.y * 800, 40, 40, color)
            else:
                this.draw(normalizedPosition.x * 1280, 800 - normalizedPosition.y * 800, 5, 5, color)
            """
    def xmbcConnect():
        this.s = socket.socket()
        host = socket.gethostname() #get localhost by default
        port = 9090
        s.connect((host,port))



    def draw(this, x, y, z, width, height, color):

        #variables describing the pointables-written above each pointable in the output
        theText = "x:" + str(x) + " \n y:" + str(y) + "\n z:" + str(z)
        this.paintCanvas.create_text(x,y, text=theText)

        #draws the ovals per pointer- i.e. what makes the finger ovals
        this.paintCanvas.create_oval( x, y, x + width, y + height, fill = color, outline = "")
        
        
        #if one of the pointables has a z value of 0 then it turns the interaction box blue
        #the z coordinate ranges from 0 to 1. If its 0 you are touching the box. 1-you are far away
        #this emulates touching a touch screen device
        if(z == 0):
            this.paintCanvas.itemconfigure(this.thisBox, fill='blue')
      
    #assigns the canvas to the object so it can be drawn upon using coordinates from the leap
    def set_canvas(this, canvas):
        this.paintCanvas = canvas

    def rgb_to_hex(this, rgb):
        return '#%02x%02x%02x' % rgb

    def paint_interaction_box(this):
        #get the attributes of the interaction box, and draw it(the box in the middle)
        height = this.interactionBox.height
        width = this.interactionBox.width
        center = this.interactionBox.center
        depth = this.interactionBox.depth

        top_left_x = 640 - width/2
        top_left_y = 400 + height/2

        bottom_right_x = 640 + width/2
        bottom_right_y = 400 - height/2
        this.thisBox = this.paintCanvas.create_rectangle(top_left_x,top_left_y,bottom_right_x,bottom_right_y )

        #was going to make a 3d visualiazation of the interaction box but fuck it 2d is good enough
        #top_left_x = 640 - width/2
        #top_left_y = 400 + height/2

        #bottom_right_x = 640 + width/2
        #bottom_right_y = 400 - height/2
        #this.paintCanvas.create_rectangle(top_left_x,top_left_y,bottom_right_x,bottom_right_y )



        #create the text describing interaction box(seen at top left of output)
        str_height = " height: " + str(height) 
        str_width  = " width: " + str(width) 
        str_center = " center: " + str(center)
        str_depth  = " depth: " + str(depth)
        boxInfo = str_height + str_width + str_center + str_depth
        this.paintCanvas.create_text(300,10,text = boxInfo)





    

def main():


        cWidth = 1280
        cHeight = 800

        #leap-sets up the leap stuff
        leapControl = Leap.Controller()
        leapControl.set_policy_flags(Leap.Controller.POLICY_BACKGROUND_FRAMES)
        theListener = TouchPointListener()
        leapControl.add_listener(theListener)

        #tkinter-create base widget for Tkinter
        master = Tk()
        master.title( "Touch Points" )
        #tkinter-add a canvas widget to the base widget, For a description of tkinter canvas api see:
        #http://effbot.org/tkinterbook/canvas.htm
        paintCanvas = Canvas(width = cWidth, height = cHeight )
        paintCanvas.pack()

        #leap-adds the canvas to the Listener object
        theListener.set_canvas(paintCanvas)

        #tkinterstarts the Tkinter main loop and destroys it when the window is closed
        #note theres weirdness here that I didn't care about becuase it's going away eventually
        master.mainloop()
        master.destroy()

if __name__ == "__main__":
    main()
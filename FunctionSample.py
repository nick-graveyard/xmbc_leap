################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import Leap, sys
import time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture


class SampleListener(Leap.Listener):
    def on_init(self, controller):
        print "Initialized"
        self.id = 0 

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        
        swipe_length = 250.0
        swipe_velocity = 750
        if(controller.config.set("Gesture.Swipe.MinLength", swipe_length)
          and controller.config.set("Gesture.Swipe.MinVelocity", swipe_velocity)):
            controller.config.save()
        
        #circle_radius = 10.0 #10.0
        #circle_arc = 0.5     #0.5
        #if(controller.config.set("Gesture.Circle.MinRadius", circle_radius)
        #  and controller.config.set("Gesture.Circle.MinArc", circle_arc)):
        #    controller.config.save()

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        self.interactionBox = frame.interaction_box
        for pointable in frame.pointables:
           # if(pointable == frame.pointables.frontmost):
           # print "handRecognized"
            for gesture in frame.gestures():
                if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                    self.callCircle(gesture, controller)
                if gesture.type == Leap.Gesture.TYPE_SWIPE:
                    self.callSwipe(gesture, controller)
                    
                if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
  	                self.callKeyTap(gesture)

                if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                    self.callScreenTap(gesture)
        
        '''
        if (frame.id%2) == 0:
           # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
            #      frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))
            
            if not frame.hands.is_empty:
                # Get the first hand
                hand = frame.hands[0]
                normalizedPosition = self.interactionBox.normalize_point(hand)
                # Check if the hand has any fingers
                fingers = hand.fingers
                if not fingers.is_empty:
                    # Calculate the hand's average finger tip position
                    avg_pos = Leap.Vector()
                    for finger in fingers:
                        avg_pos += finger.tip_position
                    avg_pos /= len(fingers)
                    # print "Hand has %d fingers, average finger tip position: %s" % (
                         # len(fingers), avg_pos)
                    

                # Get the hand's sphere radius and palm position
               # print "Hand sphere radius: %f mm, palm position: %s" % (
                     # hand.sphere_radius, hand.palm_position)

                # Get the hand's normal vector and direction
                normal = hand.palm_normal
                direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
            #print "Hand recognized"
           # print "Hand pitch: %f degrees, roll: %f degrees, yaw: %f degrees" % (
            #    direction.pitch * Leap.RAD_TO_DEG,
             #   normal.roll * Leap.RAD_TO_DEG,
              #  direction.yaw * Leap.RAD_TO_DEG)
        
  
                
                        
            if not (frame.gestures().is_empty):
                print "HandRecognized"
        '''

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

	
    def callSwipe(self, gesture, controller):
        swipe = SwipeGesture(gesture)
        if gesture.id != self.id:
            self.id = gesture.id
            #If direction is positive it's a swipe from left to right. If direction is negative it's a swipe from right to left
            if swipe.direction.x <= 0:
                swipeDirection = "Left"
            else:
                swipeDirection = "Right"
        #print "Swipe%s" % (swipeDirection)
            print "Swipe"+swipeDirection+str(controller.config.get("Gesture.Swipe.MinLength"))
            #time.sleep(.5)

    def callCircle(self, gesture, controller):
        circle = CircleGesture(gesture)

        # Determine clock direction using the angle between the pointable and the circle normal
        if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/4:
            clockwiseness = "Clockwise"
        else:
            clockwiseness = "Counterclockwise"

        # Calculate the angle swept since the last frame
        swept_angle = 0
        if circle.state != Leap.Gesture.STATE_START:
            previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
            swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI

        print "Circle%s" % (clockwiseness)


    def callKeyTap(self, gesture):
        keytap = KeyTapGesture(gesture)
        print "KeyTap"
       # print "Key Tap id: %d, %s, position: %s, direction: %s" % (
        #        gesture.id, self.state_string(gesture.state),
        #        keytap.position, keytap.direction )
	

    def callScreenTap(self, gesture):
        screentap = ScreenTapGesture(gesture)
        print "ScreenTap"
       # print "Screen Tap id: %d, %s, position: %s, direction: %s" % (gesture.id, self.state_string(gesture.state), screentap.position, screentap.direction )
	
			
def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    sys.stdin.readline()

    # Remove the sample listener when done
    controller.remove_listener(listener)


if __name__ == "__main__":
    main()

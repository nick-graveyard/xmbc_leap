import urwid
import socket


s = socket.socket()
host = socket.gethostname() #get localhost by default
port = 50000
s.connect((host,port))



def show_or_exit(key):

    #NAVIGATION
    if key in('q', 'Q'):
        s.send("close")
        raise urwid.ExitMainLoop()
    elif key =='up' :
        s.send("up")
        txt.set_text("UP")
    elif key =='down' :
        s.send("down")
        txt.set_text("DOWN") 
    elif key =='left':
        s.send("left")
        txt.set_text("LEFT") 
    elif key =='right':
        s.send("right")
        txt.set_text("RIGHT") 
    elif key =='esc':
        s.send("back")
        txt.set_text("BACK") 
    elif key =='enter':
        s.send("select")
        txt.set_text("\SELECT")
    elif key =='p':
        s.send("rightHandOn")
        txt.set_text("RIGHT HAND ON")
    elif key ==';':
        s.send("rightHandOff")
        txt.set_text("RIGHT HAND OFF")
    elif key =='o':
        s.send("leftHandOn")
        txt.set_text("LEFT HAND ON")
    elif key =='l':
        s.send("leftHandOff")
        txt.set_text("LEFT HAND OFF")
    elif key=='i':
        s.send("modeToggle")
        txt.set_text("modeToggle")


    else:
        txt.set_text(repr(key))

txt = urwid.Text(u"Hello World")
fill = urwid.Filler(txt, 'top')
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()


s.close()
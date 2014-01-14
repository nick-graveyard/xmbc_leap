import socket
import threading
from threading import *
import sys


class SimpleServer(threading.Thread):

    def __init__(self,inHost, inPort, inHandler):
        host = inHost 
        port = inPort 
        self.dataHandler = inHandler        
        #number of threads that can connect-deal with this later
        backlog = 5 
        size = 1024 
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.serversocket.bind((host,port)) 
        self.serversocket.listen(backlog) 
        
        threading.Thread.__init__(self)

         

    def run(self):
        connection, address = self.serversocket.accept()
        #connection.settimeout(10)
        while True: 
            #blocks here waiting for data
            data = connection.recv(1024) 

            if data == "close":
                print "stopping"             
                break

            if data > 0: 
                self.dataHandler.handle(data) 

             
                           
            #print "leap addon simple server looping"
        connection.close() 


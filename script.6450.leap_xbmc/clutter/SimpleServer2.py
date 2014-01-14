import SocketServer

class MyTCPHandler(SocketServer.BaseRequestHandler):

    #def __init__(self):

     #   super.__init__(self)

    """
    def setup(self):
        print "SET DIS SHIT UP"
    """

    def handle(self):
        # self.request is the TCP socket connected to the client

        self.data = self.request.recv(1024).strip()
        print "{} wrote:".format(self.client_address[0])
        print self.data

        # just send back the same data, but upper-cased
        self.request.sendall( self.data.upper() )


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    #server.allow_reuse_address=True
    #, bind_and_activate=True

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
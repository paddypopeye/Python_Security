from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(b"testing")
    
    def dataReceived(self, data):
        "Write back any data received."
        print ("Server says:", data)
        self.transport.loseConnection()
    
    def connectionLost(self, reason):
        print ("connection error")

class EchoFactory(protocol.ClientFactory):
    proto = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print ("Connection failed - goodbye!")
        reactor.stop()
    
    def clientConnectionLost(self, connector, reason):
        print ("Connection lost - goodbye!")
        reactor.stop()

def main():
    fd = EchoFactory()
    reactor.connectTCP("localhost", 8000, fd)
    reactor.run()

if __name__ == '__main__':
    main()
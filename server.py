from coapthon.server.coap import CoAP
from sensor import Sensor

class CoAPServer(CoAP):
    def __init__(self, host, port):
        CoAP.__init__(self, (host, port),multicast=False)
        self.add_resource('sensor/', Sensor())

        print "CoAP Server start on " + host + ":" + str(port)
        print self.root.dump()


def main():
    server = CoAPServer("0.0.0.0", 5683)
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print "Server Shutdown"
        server.close()
        print "Exiting..."

if __name__ == '__main__':
    main()

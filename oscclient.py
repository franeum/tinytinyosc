import socket
from tinytinyosc import *


class TinyOSCClient:
    def __init__(self, host='127.0.0.1', port=7000, protocol='udp'):
        self.host = host
        self.port = port
        self.protocol = protocol
        self.set_addr(self.host, self.port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def set_outport(self, outport=7000):
        self.port = outport
        self.set_addr((self.host, self.port))
        return 1

    def set_host(self, addr='127.0.0.1'):
        self.host = addr
        self.set_addr((self.host, self.port))
        return 1

    def set_addr(self, host='127.0.0.1', port='7000'):
        self.host = host
        self.port = port
        self.addr = (host, port)
        return 1

    def get_addr(self):
        return self.addr

    def connect(self):
        self.sock.connect(self.get_addr())
        return 1

    def bind(self):
        self.sock.bind(self.get_addr())
        return 1

    def close(self):
        self.sock.close()
        return 1

    def send(self, address, *msg):
        mess = OSCMessage(address, *msg)
        mess = mess.get_msg()
        self.sock.sendall(bytes(mess))

    def sendto(self, msg):
        self.sock.sendto(msg, self.addr)

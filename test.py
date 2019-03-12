import time
import random
from oscclient import TinyOSCClient

'''import parsemessage
from oscclient import TinyOSCClient

host = '127.0.0.1'
port = 5005
msg = parsemessage.build_whole_mess('/ciao/1/mbuto', 'bang')

sock = TinyOSCClient(host, port)
sock.connect()
sock.send(bytes(msg))
sock.close()

client = TinyOSCClient(host, port)
address = '/ciao'''

address = '/ciao/core'
msg = (10, 20)

client = TinyOSCClient('127.0.0.1', 5005)
client.connect()
for _ in range(5):
    client.send(address, 10, 20, 30, 40, 50, 60)
    time.sleep(0.2)
client.close()

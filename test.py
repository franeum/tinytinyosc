import parsemessage
from oscclient import TinyOSCClient

host = '127.0.0.1'
port = 5005
msg = parsemessage.build_whole_mess('/ciao/1/mbuto', 'bang')

sock = TinyOSCClient(host, port)
sock.connect()
sock.send(bytes(msg))
sock.close()

import parsemessage
import socket

address = ('127.0.0.1', 5005)

msg = parsemessage.build_whole_mess('/ciao', 'bang')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(bytes(msg), address)

sock.close()

__author__ = 'petro-ew'
import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s1.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s1.bind(('0.0.0.0', 11719))
while 1:
    message = s1.recv(1024)
    print(message.decode("utf-8"))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'
#import urllib
#import urllib.request
from urllib.parse import urlparse
import socket
import threading
#reload(sys)
#sys.setdefaultencoding('utf-8')
#настройки плагина 1 строка: http://127.0.0.1:88/?{name}
#                  2 строка: Incoming
#doc = urllib.request.urlopen("http://127.0.0.1:88/?number={peer}&region={name}").read()
o = urlparse("http://127.0.0.1:88/")
print(o.geturl())

host = "192.168.1.147"
port = 88

def sendproc(buffer):
    """
    :param buffer: переменная которую передаем по UDP
    """
    #print("buffer = ", buffer)
    sock1.sendto(buffer.encode("utf-8"), ('192.168.1.255', 11719))

class Connect(threading.Thread):
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        threading.Thread.__init__(self)
    def run(self):
        while True:
            buf = self.sock.recv(1024)
            if buf:
                print("ЗАШЛИ В БУФ БУФ ЕСТЬ !!!!!")
                b = buf
                b = b.decode("utf-8")
                b = b[6:18]
                b = "c" + b
                #print("из хттп:", b)
                print(b)
                sendproc(b)
        self.sock.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock1.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
while True:
    sock, addr = s.accept()
    Connect(sock, addr).start()
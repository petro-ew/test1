#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

import socket
import string
for srv in 'http', 'ftp', 'imap', 'pop3', 'smtp':
    print (socket.getservbyname(srv, 'tcp'), srv)
HOST = "127.0.0.1"
PORT = 888
BUFSIZ = 1024
ADDR = (HOST, PORT)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(ADDR)
s = ("Gravitel").encode("utf-8")
#bytes(s, "utf-8")
sock.send(s)
result = sock.recv(BUFSIZ)
sock.close()
print("Получено", result.decode('utf-8'))

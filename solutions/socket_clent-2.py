#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

import socket
import string
for srv in 'http', 'ftp', 'imap', 'pop3', 'smtp':
    print (socket.getservbyname(srv, 'tcp'), srv)
HOST = ""
PORT = 888
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.send("GRAVITEL")
result = sock.recv(1024)
sock.close()
print("Получено", result)

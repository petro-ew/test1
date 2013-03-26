#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

import socket
import string
import urllib.parse
def do_something(x):
    lst = map(None, x)
    lst.reverse()
    return string.join(lst, "")

HOST = "127.0.0.1"    #localhost
PORT = 88
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORT))
for srv2 in 'http', 'ftp', 'imap', 'pop3', 'smtp':
    print(socket.getservbyname(srv2, 'tcp'), srv2)
while 1:
    print("Слушаю порт ", PORT)
    srv.listen(1)
    sock, addr = srv._accept()

while 1:
    peer = sock.recv(1024)
    if not peer:
        break
    print("Получено от %s: %s:" % addr, peer)
    lap = do_something(peer)
    sock.send(lap)
    sock.close()

    #klient

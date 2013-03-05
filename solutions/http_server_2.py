#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

import socket
import string

def do_something(x):
    lst = map(None, x)
    lst.reverse()
    return string.join(lst, "")

HOST = ""    #localhost
PORT = 888
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind((HOST, PORT))
while 1:
    print("Слушаю порт ", PORT)
    srv.listen(1)
    sock, addr = srv._accept()

while 1:
    pal = sock.recv(1024)
    if not pal:
        break
    print("Получено от %s: %s:" % addr, pal)
    lap = do_something(pal)
    sock.send(lap)
    sock.close()

    #klient

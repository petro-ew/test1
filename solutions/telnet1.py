__author__ = 'petro-ew'

import telnetlib
import threading
import sys

class Read(threading.Thread):
    def run(self):
        while True:
            s = input()
            tn.write((s + "\r\n").encode("koi8-r"))

class Write(threading.Thread):
    def run(self):
        while True:
            piece = tn.read_some()
            print(piece.decode('koi8-r'), end='')
            sys.stdout.flush()


host = "mud.df2.ru"
tn = telnetlib.Telnet(host, 4000)
reader = Read()
writer = Write()
reader.daemon = True
writer.daemon = True
reader.start()
writer.start()
input()

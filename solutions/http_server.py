#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'petro-ew'

import http.server
import socketserver
import logging
import cgi

PORT = 888

class ServerHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            logging.error(item)
        http.server.SimpleHTTPRequestHandler.do_GET(self)
        self.send_response(200)


Handler = ServerHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()

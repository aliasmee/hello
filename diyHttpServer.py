#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import os
import socket

class changePath():
	read = str(raw_input("please enter path:"))
	PORT = int(raw_input("please enter port:"))
	os.chdir(read)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("",changePath.PORT),Handler)
print "HTTP start on %s " %PORT
httpd.serve_forever()

ip = socket.gethostbyaddr()

#! /usr/bin/env python3

# Echo client program
import socket, sys, re
from threading import Thread;

sys.path.append("/Users/dylanburdick/Desktop/OS-Labs/os-s25-filetransfer-Thedragon57/lib/")       # for params
sys.path.append("/Users/dylanburdick/Desktop/OS-Labs/s25-archiver-Thedragon57/Lab3") # for archiver
import params
import archiver, unArchiver

from encapFramedSock import EncapFramedSock


switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50000"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )


progname = "framedClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug  = paramMap["server"], paramMap["usage"], paramMap["debug"]

if usage:
    params.usage()


try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

addrFamily = socket.AF_INET
socktype = socket.SOCK_STREAM
addrPort = (serverHost, serverPort)

class Client(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        print("client started")
        sock = socket.socket(addrFamily, socktype)

        if sock is None:
            print('could not open socket')
            sys.exit(1)
        sock.connect(addrPort)
        name = sock.getsockname()
        print(f"client {name} connected")
        fsock = EncapFramedSock((sock, name))
        fsock.send(archiver.folderArchiver("/Users/dylanburdick/Desktop/OS-Labs/s25-archiver-Thedragon57/testFiles"), debug)
        print(f"client {name} received:", fsock.receive(debug))

        #fsock.send( b"hello world", debug)
        fsock.shutdown()
        #print(f"client {name} received:", fsock.receive(debug))

        fsock.close()
        print(f"client {name} done")

clients = [ Client() for _ in range(3) ]
for c in clients:
    c.start()

for c in clients:
    c.join()
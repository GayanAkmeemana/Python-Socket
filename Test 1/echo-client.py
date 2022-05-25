#!/usr/bin/env python3

import socket
IP = "127.0.0.1" #loopback
PORT = 65432 #non-privilaged ports > 1023
AMT_DATA = 1024

#socket created socket()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    mySocket.connect((IP, PORT))
    mySocket.sendall(b"Hello from Gayan -->")
    data = mySocket.recv(AMT_DATA)

print("Received ", repr(data))
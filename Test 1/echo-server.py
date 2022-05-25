#!/usr/bin/env python3

import socket
IP = "127.0.0.1" #loopback
PORT = 65432 #non-privilaged ports > 1023
AMT_DATA = 1024

#socket created socket()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
    #bint the socket with proper IP and a port bind()
    mySocket.bind((IP, PORT)) 
    #listning socket listen()
    mySocket.listen()
    #blocking mode accept()
    conn, addr = mySocket.accept()
    with conn:
        print("connected by: ", addr)
        while True:
            data = conn.recv(AMT_DATA)
            if not data:
                break
            conn.sendall(data)










#send and receive data


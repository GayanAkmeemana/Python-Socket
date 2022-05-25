# server code
import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 8094
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MSG = " GOTDISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

print(socket.gethostbyname(socket.gethostname()))

def incoming_clients(conn, addr):
    print("client {addr} connected")
    condition = True
    while condition:
        length_msg = conn.recv(HEADER).decode(FORMAT)
        if length_msg:
            length_msg = int (length_msg)
            message = conn.recv(length_msg).decode(FORMAT)
            if(message) == DISCONNECT_MSG:
                condition = False
            print (f"{addr} {message}")
            conn.send("Message Received Loud and Clear".encode(FORMAT))
    conn.close()


def setupServer():
    server.listen()
    print("Echo Server is now listning")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target= incoming_clients, args=(conn, addr))
        thread.start()
        print("[Incoming Connections] {threading.activeCount() - 1")

print("[Server] is starting....")
setupServer()
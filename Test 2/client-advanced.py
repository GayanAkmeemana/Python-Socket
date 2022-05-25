# client code
import socket

SERVER = "192.168.56.1"
PORT = 8094
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MSG = " GOTDISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def client_send(message):
    message = message.encode(FORMAT)
    length_msg = len(message)
    length_send = str(length_msg).encode(FORMAT)
    length_send += b' ' * (HEADER - len(length_send))
    client.send(length_send)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

client_send("Hello Gayan")
input()
client_send("How are you?")
input()
client_send(DISCONNECT_MSG)
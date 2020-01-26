"""Client to connect to server"""
import socket

port = 6896
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', port))
while True:
    client_socket.send(b'Hi\n')
    message = client_socket.recv(4096)
    if message == bytes('Hi\n', "utf-8"):
        print(str(message, "utf-8"))
        break

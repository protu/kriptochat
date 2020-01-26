"""Server that will listen for client to begin chat"""
import socket
import struct

port = 6896
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', port))
server_socket.listen(1)

str_msg = "Hi\n"
msg = struct.pack('!I', len(str_msg)) + bytes(str_msg, "utf-8")

while True:
    (client_socket, address) = server_socket.accept()
    data = client_socket.recv(4096)
    client_socket.send(data)

server_socket.shutdown(1)
server_socket.close()

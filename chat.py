import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 6001))
sock.listen(1)
connections = []


def handler(c, a):
    while True:
        data = c.recv(1024)
        for connection in connections:
            connection.send(data)
        if not data:
            break


while True:
    c, a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c, a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)

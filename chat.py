import socket
import threading


class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('0.0.0.0', 6001))
        self.sock.listen(1)


    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                break


    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(self.connections)

import socket
import threading
import sys


class Server:
    connections = []
    peers = []
    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
        sock.bind(('0.0.0.0', 6001))
        sock.listen(1)
        print("Server started...")
        while True:
                    c, a = sock.accept()
                    cThread = threading.Thread(target=self.handler, args=(c, a))
                    cThread.daemon = True
                    cThread.start()
                    self.connections.append(c)
                    self.peers.append(a[0])
                    print(str(a[0]) + ":" + str(a[1]), "connected")
                    self.sendPeers()


    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ":" + str(a[1]), "disconnected")
                self.connections.remove(c)
                self.peers.remove(a[0])
                c.close()
                self.sendPeers()
                break
    

    def sendPeers(self):
        p = ""
        for peer in self.peers:
            p = p  + peer + ","
        
        for connection in self.connections:
            connection.send(b'\x11' + bytes(p, 'utf-8'))

class Client:

    def __init__(self, address):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((address, 6001))
        iThread = threading.Thread(target=self.sendMsg, args=(sock, ))
        iThread.daemon = True
        iThread.start()

        while True:
            data = sock.recv(1024)
            if not data:
                break
            if data[:1] == b'\x11':
                print("got peers")
            else:
                print(str(data, 'utf-8'))

    def sendMsg(self, sock):
        while True:
            sock.send(bytes(input(": "), 'utf-8'))


if len(sys.argv) > 1:
    client = Client(sys.argv[1])
else:
    server = Server()

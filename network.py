import socket, pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.49.248"
        self.port = 12345
        self.addr = (self.server, self.port)

    def GetData(self):
        return pickle.loads(self.client.recv(4096))

    def connect(self):
        self.client.connect(self.addr)
        return pickle.loads(self.client.recv(4096))

    def send(self, Players,Game):
        self.client.sendall(pickle.dumps([Players,Game]))

        return pickle.loads(self.client.recv(4096))

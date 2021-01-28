import socket, pickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.49.248"
        self.port = 12345
        self.addr = (self.server, self.port)

    def GetData(self):
        Data1 = pickle.loads(self.client.recv(4096))
        Data2 = pickle.loads(self.client.recv(4096))
        return Data1, Data2

    def connect(self):
        self.client.connect(self.addr)
        return pickle.loads(self.client.recv(4096))

    def send(self, Players,Game):
        Data1 = pickle.loads(self.client.recv(4096))
        Data2 = pickle.loads(self.client.recv(4096))

        self.client.sendall(pickle.dumps(Players))
        self.client.sendall(pickle.dumps(Game))

        return Data1, Data2
import socket
import pickle


class Network:

    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (self.server, self.port)

        self.player = self.connect()
        # print(self.pos)

    def get_player(self):
        return self.player

    def connect(self):
        """Метод подключения клиента к серверу."""
        try:
            self.client.connect(self.address)
            return pickle.loads(self.client.recv(2048))
        except:
            print('Connection error appeared')

    def send(self, data):
        """Метод по отправке информации на сервер."""
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)


# if __name__ == "__main__":
#     network = Network("", 5555)
#     network.send("hello")
#     network.send("world")

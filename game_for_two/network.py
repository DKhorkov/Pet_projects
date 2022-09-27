import socket


class Network:

    def __init__(self, server, port):
        self.server = server
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (self.server, self.port)

        self.pos = self.connect()  # Получаем позицию игрока
        # print(self.pos)

    def get_pos(self):
        return self.pos

    def connect(self):
        """Метод подключения клиента к серверу."""
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            print('Connection error appeared')

    def send(self, data):
        """Метод по отправке информации на сервер."""
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)


# if __name__ == "__main__":
#     network = Network("", 5555)
#     network.send("hello")
#     network.send("world")

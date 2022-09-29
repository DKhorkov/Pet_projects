import socket
from _thread import start_new_thread
import pickle

from player import Player1, Player2
from settings import Settings


class Server:

    def __init__(self, server, port, num_to_listen):
        self.settings = Settings()
        self.players = [Player1(self.settings.square_1_x, self.settings.square_1_y, self.settings.square_face,
                                self.settings.square_1_color),
                        Player2(self.settings.square_2_x, self.settings.square_2_y, self.settings.square_face,
                                self.settings.square_2_color)]
        self.server = server
        self.port = port
        self.num_to_listen = num_to_listen
        self.current_player = 0

    def __create_socket(self):
        """Создаем соккет для приема соединений от пользователей."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
        self.socket.bind((self.server, self.port))  # связываем сокет с портом, где он будет ожидать сообщения
        self.socket.listen(self.num_to_listen)

    def __create_thread_for_client(self, connection, player):
        """Создаем поток для обработки информации от пользователя, которая должна прийти на сервер для обработки,
        но не должна заставлять программу подвисать в основном цикле, пока вычисляется инфа."""
        connection.send(pickle.dumps(self.players[player]))  # Записываем объект в файл
        self.reply = ""  # Создаем переменную для ответа от сервера
        while True:
            try:
                self.data = pickle.loads(connection.recv(2048))  # Загружаем объект из файла
                self.players[player] = self.data

                # Если клиент ничего не отправляет на сервер - выводим инфу о том, что он отключился и заканчиваем цикл.
                if not self.data:
                    print('Client has disconnected')
                    break
                else:
                    if player == 1:
                        self.reply = self.players[0]
                    else:
                        self.reply = self.players[1]
                    print(f'Received: {self.data}')
                    print(f'Sending: {self.reply}')

                connection.sendall(pickle.dumps(self.reply))  # Отправка обратно закодированных данных нашему серверу
            except:
                print('Some error appeared')
                break

        # Закрываем соединение с сервером:
        print('Connection was closed')
        connection.close()

    def main(self):
        print("Server is working")
        self.__create_socket()
        while True:
            self.conn, self.addr = self.socket.accept()  # начинаем принимать соединения
            print(f'Connected to server with the address {self.addr}.')
            start_new_thread(self.__create_thread_for_client, (self.conn, self.current_player))
            self.current_player += 1  # Апдейтим инфу, что у нас подключился пользователь


if __name__ == "__main__":
    server = Server("", 5555, 2)
    server.main()

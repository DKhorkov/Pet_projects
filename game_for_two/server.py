import socket
import os
from _thread import start_new_thread


class Server:

    def __init__(self, server, port, num_to_listen):
        self.positions = [(0, 0), (200, 200)]
        self.server = server
        self.port = port
        self.num_to_listen = num_to_listen
        self.current_player = 0

    def read_pos(self, string):
        """Поскольку отправялем на сервер строки, необходимо их обработать для изменения позиции квадрата"""
        strn = string.split(",")
        return int(strn[0]), int(strn[1])

    def make_pos(self, tup):
        """Для отправки инфы на сервер, необходимо преобразовать ее в строку"""
        return str(tup[0]) + "," + str(tup[1])

    def __create_socket(self):
        """Создаем соккет для приема соединений от пользователей."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
        self.socket.bind((self.server, self.port))  # связываем сокет с портом, где он будет ожидать сообщения
        self.socket.listen(self.num_to_listen)

    def __create_thread_for_client(self, connection, player):
        """Создаем поток для обработки информации от пользователя, которая должна прийти на сервер для обработки,
        но не должна заставлять программу подвисать в основном цикле, пока вычисляется инфа."""
        connection.send(str.encode(self.make_pos(self.positions[player])))
        self.reply = ""  # Создаем переменную для ответа от сервера
        while True:
            try:
                self.data = self.read_pos(connection.recv(2048).decode())  # принимаем данные от клиента, по 1024 байт
                # self.reply = self.data.decode('UTF-8')
                self.positions[player] = self.data

                # Если клиент ничего не отправляет на сервер - выводим инфу о том, что он отключился и заканчиваем цикл.
                if not self.data:
                    print('Client has disconnected')
                    break
                else:
                    if player == 1:
                        self.reply = self.positions[0]
                    else:
                        self.reply = self.positions[1]
                    print(f'Received: {self.data}')
                    print(f'Sending: {self.reply}')

                connection.sendall(str.encode(self.make_pos(self.reply)))  # Отправка обратно закодированных данных нашему серверу
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
    server = Server("192.168.0.111", 5555, 2)
    server.main()

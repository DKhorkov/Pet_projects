import socket
import os
from _thread import start_new_thread


class Server:

    def __init__(self, server, port, num_to_listen):
        self.server = server
        self.port = port
        self.num_to_listen = num_to_listen

    def __create_socket(self):
        """Создаем соккет для приема соединений от пользователей."""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # создаем сокет
        self.socket.bind((self.server, self.port))  # связываем сокет с портом, где он будет ожидать сообщения
        self.socket.listen(self.num_to_listen)

    def __create_thread_for_client(self, connection):
        """Создаем поток для обработки информации от пользователя, которая должна прийти на сервер для обработки,
        но не должна заставлять программу подвисать в основном цикле, пока вычисляется инфа."""
        connection.send(str.encode('Connected to server'))  # Оповещаем юзера, что он подключился к серверу
        self.reply = ""  # Создаем переменную для ответа от сервера
        while True:
            try:
                self.data = connection.recv(2048)  # принимаем данные от клиента, по 1024 байт
                self.reply = self.data.decode('UTF-8')

                # Если клиент ничего не отправляет на сервер - выводим инфу о том, что он отключился и заканчиваем цикл.
                if not self.data:
                    print('Client has disconnected')
                    break
                else:
                    print(f'Received: {self.reply}')

                connection.sendall(str.encode(self.reply))  # Отправка обратно закодированных данных нашему серверу
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
            start_new_thread(self.__create_thread_for_client, (self.conn,))


if __name__ == "__main__":
    server = Server("", 5555, 2)
    server.main()

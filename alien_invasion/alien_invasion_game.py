import sys
import pygame

from settings import Settings
from ship import Ship


# Для создания пустого окна, в котором будет запускаться игра создадим класс:
class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализация игры и ресурсов."""
        pygame.init()  # Команда для запуска в работу библиотеки 'pyGame'.

        self.settings = Settings()
        self.screen = pygame.display.set_mode((1600, 900))  # Двойные скобки, ибо устанавливаем только размер экрана.
        pygame.display.set_caption('Alien Invasion')  # Устанавливает название окна игры.
        self.ship = Ship(self.screen)  # Передаем атрибуту 'ship' атрибут экрана.

    def __check_events(self):  # Делаем метод приватным.
        """Проверяет события в программе."""
        for event in pygame.event.get():  # Идентифицирует каждое событие в программе.
            if event.type == pygame.QUIT:  # Если пользователь нажал кнопку закрытия программы, то игра закроется.
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Если нажать кнопку, корабль начнет движение.
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
            elif event.type == pygame.KEYUP:  # Если отпустить кнопку, то корабль перестанет двигаться.
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False

    def __update_screen(self):  # Делаем метод приватным.
        """Обновляет изображение на экране."""
        self.screen.fill(self.settings.bg_color)  # Обновление цвета экрана перед выводом пользователю.
        self.ship.show_ship()  # Выводим корабль на экран.
        pygame.display.flip()  # Обновляет экран пользователя после установления цвета и вывода корабля.

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание действий пользователя на клавиатуре или с помощью мыши. Если "выход", то закрыть игру.
            self.__check_events()
            self.ship.update_ship_position()
            self.__update_screen()


if __name__ == '__main__':
    the_game = AlienInvasion()
    the_game.run_game()

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullets
from alien import Alien


# Для создания пустого окна, в котором будет запускаться игра создадим класс:
class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализация игры и ресурсов."""
        pygame.init()  # Команда для запуска в работу библиотеки 'pyGame'.

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption('Alien Invasion')  # Устанавливает название окна игры.
        self.ship = Ship(self.screen)  # Передаем атрибуту 'ship' атрибут экрана.
        self.bullets = pygame.sprite.Group()  # Создаем "список", хранящий в себе выпущенные снаряды.
        self.aliens = pygame.sprite.Group()  # Создаем "список", хранящий в себе пришельцев.
        self.__create_fleet()

    def __check_keydown_events(self, event):
        """Проверяет события при нажатии клавиш."""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:  # Второй способ для пользователя закрыть программу, нажав 'q'.
            sys.exit()
        if event.key == pygame.K_SPACE:  # Стреляем снарядами при нажатии пробела.
            self.__fire_bullet()

    def __check_keyup_events(self, event):
        """Проверяет события при отпускании клавиш."""
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def __check_events(self):  # Делаем метод приватным.
        """Проверяет события в программе."""
        for event in pygame.event.get():  # Идентифицирует каждое событие в программе.
            if event.type == pygame.QUIT:  # Если пользователь нажал кнопку закрытия программы, то игра закроется.
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # Если нажать кнопку, корабль начнет движение.
                self.__check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # Если отпустить кнопку, то корабль перестанет двигаться.
                self.__check_keyup_events(event)

    def __create_alien(self, alien_number, alien_row):
        """Создает одного пришельца."""
        alien = Alien(self.screen, self.settings)
        alien_width, alien_height = alien.rect.size
        alien.x = 0.05 * alien_width + 2 * alien_width * alien_number  # Создает сдвиг каждого нового пришельца вправо.
        alien.y = 0 * alien_height + 2 * alien_height * alien_row  # Расстояние между рядами.
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)  # Добавляем созданный экземпляр в группу пришельцев.

    def __create_fleet(self):
        """Создает флот пришельцев."""
        alien = Alien(self.screen, self.settings)  # Создаем экземпляр класса пришельца.
        alien_width, alien_height = alien.rect.size  # Множественное присвоение.
        # Ниже представлен отступ с правой стороны экрана. Он нужен для дальнейшего движения ряда вправо.
        available_space_x = self.settings.screen_width - (10 * alien_width)
        # (2 * alien_width) - отступ от пришельца (равный ширине) + создание нового пришельца = 2 ширинам пришельца.
        number_of_aliens_x = available_space_x // (2 * alien_width)

        # Определим, сколько рядов пришельцев можно уместить на экране до корабля.
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (2 * alien_height) - ship_height
        number_of_alien_rows_y = available_space_y // (2 * alien_height)

        # Создадим много рядов (флот) пришельцев:
        for alien_row in range(number_of_alien_rows_y):
            for alien_number in range(number_of_aliens_x):
                self.__create_alien(alien_number, alien_row)

    def __fire_bullet(self):
        """Создание выстрела пулей и включение пули в группу."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullets(self.screen, self.settings, self.ship)
            self.bullets.add(new_bullet)

    def __change_fleet_direction(self):
        """Меняет направление движения флота при достижении края."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def __check_fleet_edges(self):
        """Проверяет, не достиг ли флот одного из краев экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.__change_fleet_direction()
                break

    def __update_aliens(self):
        """Обновляет местоположение всех пришельцев."""
        self.__check_fleet_edges()
        self.aliens.update()

    def __update_bullets(self):
        """Обновляет снаряды и удаляет ненужные снаряды."""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.top <= 0:  # Если верх пули достигает верхней части экрана, пуля удаляется из игры.
                self.bullets.remove(bullet)

    def __update_screen(self):  # Делаем метод приватным.
        """Обновляет изображение на экране."""
        self.screen.fill(self.settings.bg_color)  # Обновление цвета экрана перед выводом пользователю.
        self.ship.show_ship()  # Выводим корабль на экран.
        for bullet in self.bullets.sprites():  # Перебираем всю группу снарядов и рисуем каждый снаряд.
            bullet.draw_bullet()
        for elien in self.aliens.sprites():
            elien.show_alien()
        pygame.display.flip()  # Обновляет экран пользователя после установления цвета и вывода корабля с пулями.

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслеживание действий пользователя на клавиатуре или с помощью мыши. Если "выход", то закрыть игру.
            self.__check_events()
            self.ship.update_ship_position()
            self.__update_aliens()
            self.__update_bullets()  # Пули после корабля, ибо позиция их должна меняться после изменения поз. корабля.
            self.__update_screen()


if __name__ == '__main__':
    the_game = AlienInvasion()
    the_game.run_game()

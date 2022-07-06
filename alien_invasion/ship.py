"""Класс корабля для использования в игре Alien Invasion."""
import pygame


class Ship:
    """Корабль-Миша для борьбы с инопланетными Полинами."""

    def __init__(self, screen):
        """Инициализация корабля и установление его изначальной позиции."""
        # Присвоение экрана экземпляра класса 'AlienInvasion' атрибуту класса Ship для дальнейшего обращения.
        self.screen = screen
        self.screen_rect = screen.get_rect()  # Создаем прямоугольник экрана.

        # Загрузим картинку, которая будет использоваться как корабль (форма прямоугольник):
        self.image = pygame.image.load('images/ship3.bmp')
        self.image.set_colorkey('black')  # Сделали прозрачным фон изображения, у которых цвет пикселей черный.
        self.rect = self.image.get_rect()  # Создаем прямоугольник с нашим изображением.
        self.rect.midbottom = self.screen_rect.midbottom  # Корабль появится внизу посередине.

        # Создадим флаги для движения корабля
        self.moving_right = False
        self.moving_left = False

    def update_ship_position(self):
        """Обновляет местонахождение корабля в зависимости от нажатия на кнопки пользователем."""
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1

    def show_ship(self):
        """Выводит изображение корабля в текущей позиции."""
        self.screen.blit(self.image, self.rect)


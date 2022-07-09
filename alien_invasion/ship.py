"""Класс корабля для использования в игре Alien Invasion."""
import pygame
from pygame.sprite import Sprite

from settings import Settings


class Ship(Sprite):
    """Корабль-Миша для борьбы с инопланетными Полинами."""

    def __init__(self, screen, picture):
        """Инициализация корабля и установление его изначальной позиции."""
        super().__init__()
        # Присвоение экрана экземпляра класса 'AlienInvasion' атрибуту класса Ship для дальнейшего обращения.
        self.screen = screen
        self.screen_rect = screen.get_rect()  # Создаем прямоугольник экрана.

        # Загрузим картинку, которая будет использоваться как корабль (форма прямоугольник):
        # self.image = pygame.image.load('images/ship3.bmp') - было так, но тогда жизни и корабль одного размера.
        self.image = pygame.image.load(picture)
        self.image.set_colorkey('black')  # Сделали прозрачным фон изображения, у которых цвет пикселей черный.
        self.rect = self.image.get_rect()  # Создаем прямоугольник с нашим изображением.
        self.ship_start_position()

        # Создадим флаги для движения корабля
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.settings = Settings()

    def update_ship_position(self):
        """Обновляет местонахождение корабля в зависимости от нажатия на кнопки пользователем."""
        if self.moving_right and self.rect.right < self.screen_rect.right:  # Нельзя выйти за правую часть экрана.
            self.rect.x += self.settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:  # Нельзя выйти за левую часть экрана.
            self.rect.x -= self.settings.ship_speed_factor
        elif self.moving_up and self.rect.top > self.screen_rect.top:  # Нельзя выйти за левую часть экрана.
            self.rect.y -= self.settings.ship_speed_factor / 2
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:  # Нельзя выйти за левую часть экрана.
            self.rect.y += self.settings.ship_speed_factor / 2

    def ship_start_position(self):
        """Размещает корабль в изначальном положении."""
        self.rect.midbottom = self.screen_rect.midbottom  # Корабль появится внизу посередине.
        self.x = float(self.rect.x)

    def show_ship(self):
        """Выводит изображение корабля в текущей позиции."""
        self.screen.blit(self.image, self.rect)

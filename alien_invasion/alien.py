"""Создание класса пришельца в отдельном модуле."""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Создание класса пришельца для игры Alien Invasion."""

    def __init__(self, screen, settings):
        """Инициализация пришельца и его стартовой позиции на экране."""
        super().__init__()
        self.screen = screen
        self.settings = settings

        # Загружаем изображение и делаем его прямоугольником
        self.alien_image = pygame.image.load('images/alien.bmp')
        self.alien_image.set_colorkey('black')  # Сделали прозрачным фон изображения, у которых цвет пикселей черный.
        self.rect = self.alien_image.get_rect()

        # # Пришелец появляется в верхнем левом углу с отступом от начала координат.
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height

        # Сохранение точной горизонтальной позиции пришельца:
        self.x = float(self.rect.x)

    def update(self):  # Чтобы флот двигался, метод должен быть назван именно 'update'.
        """Перемещение пришельцев вправо."""
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x

    def show_alien(self):
        """Выводит изображение пришельца в текущей позиции."""
        self.screen.blit(self.alien_image, self.rect)

    def check_edges(self):
        """Возвращает True, если пришелец достиг края."""
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right) or (self.rect.left <= 0):
            return True

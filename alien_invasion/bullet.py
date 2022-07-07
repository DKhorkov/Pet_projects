"""Класс снарядов, летящих в пришельцев в игре Alien Invasion."""

import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    """Класс для управления снарядов, выпущенных кораблем."""

    def __init__(self, screen, settings, ship):
        """Создает снаряд в текущей позиции корабля."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.color = self.settings.bullet_color

        # Установление изначальной позиции снаряда
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.topleft = ship.rect.topleft  # Меняем изначальное расположение снарядов (ставим их в верх корабля).
        self.rect.left += 15  # Сдвигаем левый снаряд чуть правее, чтобы он летел из глаза.
        self.y = float(self.rect.y)
        self.rect2 = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect2.topright = ship.rect.topright
        self.rect2.right -= 17  # Сдвигаем правый снаряд чуть левее, чтобы он летел из глаза.
        self.y2 = float(self.rect2.y)

    def update(self):  # Чтобы пули летели, метод должен быть назван именно 'update'.
        """Обновляет местонахождение снаряда, который летит вверх по экрану."""
        self.y -= self.settings.bullet_speed  # Обновление позиции снаряда.
        self.rect.y = self.y  # Обновляет позицию прямоугольника снаряда.
        self.y2 -= self.settings.bullet_speed
        self.rect2.y = self.y2

    def draw_bullet(self):
        """Выводит снаряд на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.color, self.rect2)

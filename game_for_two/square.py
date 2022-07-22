import pygame
from pygame.sprite import Sprite


class Square(Sprite):
    """Квадрат для игры."""

    def __init__(self, screen, settings, color):
        """Атрибуты корабля."""
        super().__init__()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.setting = settings
        self.lives = self.setting.lives
        self.color = color

        self.rect = pygame.Rect(0, 0, self.setting.square_face, self.setting.square_face)

    def square_moving(self, moving_up, moving_down):
        """Изменение положения квадрата"""
        if moving_up and self.rect.top > 50:
            self.rect.y -= self.setting.square_speed
        elif moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.setting.square_speed

    def draw_square(self):
        """Рисует квадрат на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)

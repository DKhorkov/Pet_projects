import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс пули для игры."""

    def __init__(self, screen, settings):
        """Инициализация атрибутов пули."""
        super().__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.settings = settings

        self.rect = pygame.Rect(0, 0, self.settings.bullet_widht, self.settings.bullet_height)
        self.color = self.settings.bullet_color

    def bullet_start_position_1(self, square):
        """Первая изначальная позиция для расположения пули."""
        self.rect.left = square.rect.right
        self.rect.centery = square.rect.centery

    def bullet_start_position_2(self, square):
        """Первая изначальная позиция для расположения пули."""
        self.rect.right = square.rect.left
        self.rect.centery = square.rect.centery

    def update_bullet_position_1(self):
        """Полет пули из первой позиции."""
        self.rect.x += self.settings.bullet_speed

    def update_bullet_position_2(self):
        """Полет пули из первой позиции."""
        self.rect.x -= self.settings.bullet_speed

    def draw_bullet(self):
        """Рисует пулю на экране."""
        pygame.draw.rect(self.screen, self.color, self.rect)

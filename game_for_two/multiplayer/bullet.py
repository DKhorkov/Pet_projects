import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс пули для игры."""

    def __init__(self, settings):
        """Инициализация атрибутов пули."""
        super().__init__()
        self.settings = settings

        self.rect = pygame.Rect(0, 0, self.settings.bullet_widht, self.settings.bullet_height)
        self.color = self.settings.bullet_color

    def bullet_start_position_1(self, square):
        """Первая изначальная позиция для расположения пули."""
        self.rect.left = square[0] + self.settings.square_face
        self.rect.centery = square[1] + self.settings.square_face / 2

    def bullet_start_position_2(self, square):
        """Первая изначальная позиция для расположения пули."""
        self.rect.left = square[0] - self.settings.bullet_widht
        self.rect.centery = square[1] + self.settings.square_face / 2

    def update_bullet_position_1(self):
        """Полет пули из первой позиции."""
        self.rect.x += self.settings.bullet_speed

    def update_bullet_position_2(self):
        """Полет пули из первой позиции."""
        self.rect.x -= self.settings.bullet_speed

    def draw_bullet(self, screen):
        """Рисует пулю на экране."""
        pygame.draw.rect(screen, self.color, self.rect)

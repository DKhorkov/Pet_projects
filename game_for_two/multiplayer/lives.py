import pygame
from pygame.sprite import Sprite


class Lives(Sprite):
    """Класс для рисования жизней игроков."""

    def __init__(self, screen):
        """Атрибуты жизней."""
        super().__init__()

        self.screen = screen
        self.image = pygame.image.load('lives.bmp')
        self.image.set_colorkey('black')
        self.rect = self.image.get_rect()

    def show_lives(self):
        """Вывод жизней на экран."""
        self.screen.blit(self.image, self.rect)

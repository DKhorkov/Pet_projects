import pygame
import pygame.font


class Button:
    """Кнопка в игре"""

    def __init__(self, screen, text):
        """Атрибуты кнопки"""
        pygame.init()

        self.text = text

        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.button_width = 80
        self.button_height = 50
        self.button_color = 'white'
        self.font = pygame.font.SysFont(None, 40)
        self.rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.rect.center = self.screen_rect.center

        self.text_button()

    def text_button(self):
        """Создание текста кнопки в виде картинки"""
        self.image = self.font.render(self.text, True, self.button_color, 'black')
        self.image_rect = self.image.get_rect()
        self.image_rect.center = self.screen_rect.center

    def draw_button(self):
        """Рисует кнопку на экране"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.image, self.image_rect)
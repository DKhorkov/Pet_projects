"""Класс для создания кнопки на экране."""
import pygame.font  # Модуль для вывода текста на экран
import pygame


class Button:
    """Класс кнопки на экране."""

    def __init__(self, screen, text):
        """Инициализация атрибутов кнопки."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # Установим размер и свойства кнопки:
        self.width, self.height = 200, 50
        self.button_color = (255, 0, 0)
        self.text_color = (255, 215, 0)
        self.font = pygame.font.SysFont(None, 48)  # Шрифт по умолчанию, размер текста 48.

        # Создание квадрата кнопки по центру экрана:
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center  # Настройка местоположения кнопки на экране.

        # Сообщение кнопки создается только один раз.
        self.button_text(text)

    def button_text(self, text):
        """Преобразует полученный текст в прямоугольник и выравнивает по центру."""
        self.text_image = self.font.render(text, True,  self.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        """Рисует кнопку на экране."""
        self.screen.fill(self.button_color, self.rect)  # Рисует прямоугольник для кнопки.
        self.screen.blit(self.text_image, self.text_image_rect)  # Выводит текст в прямоугольнике кнопки.

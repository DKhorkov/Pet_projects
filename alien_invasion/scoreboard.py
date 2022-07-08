"""Класс для представления очков игрока."""
import pygame.font


class Scoreboard:
    """Класс для вывода очков игрока."""

    def __init__(self, screen, settings, stats):
        """Инициализация атрибутов подсчета очков."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings
        self.stats = stats

        # Настройка шрифта для вывода счета
        self.text_color = (245, 255, 250)
        self.font = pygame.font.SysFont(None, 40)  # Шрифт и размер текста очков.

        self.draw_score()  # Преобразуем текст в изображение.

    def draw_score(self):
        """Рисует количество очков."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, 'black')

        # Вывод счета в верхнем правом углу экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 15
        self.score_rect.top = 20

    def show_score(self):
        """Выводит изображение счета на экран игрока."""
        self.screen.blit(self.score_image, self.score_rect)

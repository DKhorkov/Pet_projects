import pygame.image
from pygame import font
from pygame.sprite import Group

from lives import Lives


class Scoreboard:
    """Класс игровой статистики."""

    def __init__(self, screen, settings, first_square, second_square):
        """Инициализация атрибутов игровой статистики."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.settings = settings

        self.first_square = first_square
        self.second_square = second_square

        self.text_color = 'white'
        self.font = font.SysFont(None, 30)

        self.draw_first_square_lives()
        self.draw_second_square_lives()

    def draw_first_square_lives(self):
        """Рисует жизни первого квадрата."""
        first_square_lives_str = "FIRST PlAYER'S LIVES:"
        self.first_square_lives_image = self.font.render(first_square_lives_str, True, self.text_color, 'black')

        self.firest_square_lives_rect = self.first_square_lives_image.get_rect()
        self.firest_square_lives_rect.left = 20
        self.firest_square_lives_rect.top = 20

        self.p_1_lives = Group()
        for live_number in range(self.first_square.lives):
            live = Lives(self.screen)
            live.rect.x = self.firest_square_lives_rect.right + live_number * (live.rect.width + 15)
            live.rect.y = 0
            self.p_1_lives.add(live)

    def draw_second_square_lives(self):
        """Рисует жизни первого квадрата."""
        second_square_lives_str = "SECOND PlAYER'S LIVES:"
        self.second_square_lives_image = self.font.render(second_square_lives_str, True, self.text_color, 'black')

        self.second_square_lives_rect = self.second_square_lives_image.get_rect()
        self.second_square_lives_rect.right = self.screen_rect.right - 200
        self.second_square_lives_rect.top = 20

        self.p_2_lives = Group()
        for live_number in range(self.second_square.lives):
            live = Lives(self.screen)
            live.rect.x = self.second_square_lives_rect.right + live_number * (live.rect.width + 15)
            live.rect.y = 0
            self.p_2_lives.add(live)

    def show_lives(self):
        """Выводит на экран картинки жизней квадратов игроков."""
        self.screen.blit(self.first_square_lives_image, self.firest_square_lives_rect)
        self.screen.blit(self.second_square_lives_image, self.second_square_lives_rect)
        self.p_1_lives.draw(self.screen)
        self.p_2_lives.draw(self.screen)

# Игра с квадартами для двоих.
import pygame

from settings import Settings


class GameForTwo:
    """Класс для запуска игры."""

    def __init__(self):
        """Атрибуты игры."""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Square game for two')

    def run_game(self):
        """Запуск игры."""
        while True:
            pygame.display.flip()


if __name__ == '__main__':
    game = GameForTwo()
    game.run_game()


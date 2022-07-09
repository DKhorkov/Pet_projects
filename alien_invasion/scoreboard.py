"""Класс для представления очков игрока."""
import pygame.font
import json
from pygame.sprite import Group

from ship import Ship


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
        self.draw_record()  # Преобразует рекорд в изображение.
        self.draw_level()  # Преобразует уровень в изображение.
        self.draw_ships()

    def draw_score(self):
        """Рисует количество очков."""
        rounded_score = round(self.stats.score, -1)  # -1 для округления до ближайшего десятка.
        score_str = f'SCORE: {"{:,}".format(rounded_score)}'  # Делаем формат очков с запятыми между тысячами (1,000).
        self.score_image = self.font.render(score_str, True, self.text_color, 'black')

        # Вывод счета в верхнем правом углу экрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 15
        self.score_rect.top = 20

    def draw_record(self):
        """Рисует рекорд в игре."""
        rounded_record = round(self.stats.record, -1)
        record_str = f'RECORD: {"{:,}".format(rounded_record)}'
        self.record_image = self.font.render(record_str, True, self.text_color, 'black')

        # Вывод рекорда посередине сверху:
        self.record_rect =self.record_image.get_rect()
        self.record_rect.midtop = self.screen_rect.midtop
        self.record_rect.top = 20

    def draw_level(self):
        """Выводит изображение уровня."""
        level_str = f'LVL: {str(self.stats.level)}'
        self.level_image = self.font.render(level_str, True, self.text_color, 'black')  # Создание изображения.

        # Ниже определяем, где будет выведено значение уровня:
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        """Выводит изображение счета на экран игрока."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.record_image, self.record_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.ships_left_image, self.ships_left_rect)
        self.ships.draw(self.screen)

    def check_record(self):
        """Проверяет, не побит ли рекорд."""
        if self.stats.score > self.stats.record:
            self.stats.record = self.stats.score
            with open('record.txt', "w") as f:
                json.dump(self.stats.record, f)
            self.draw_record()

    def draw_ships(self):
        """Рисует количество оставшихся жизней (кораблей) на экране."""
        self.ships_left_image = self.font.render('LIVES LEFT:', True, self.text_color, 'black')
        self.ships_left_rect = self.ships_left_image.get_rect()
        self.ships_left_rect.left = 10
        self.ships_left_rect.top = 10

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, 'images/ship_life.bmp')
            ship.rect.x = 180 + ship_number * (ship.rect.width + 20)
            ship.rect.y = 0
            self.ships.add(ship)


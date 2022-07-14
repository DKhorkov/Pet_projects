"""Класс настроек игры."""
import pygame.image


class Settings:
    """Класс для настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализация статических настроек игры."""
        # Настройки экрана:
        self.bg_color = pygame.image.load('images/space.bmp')
        self.screen_width = 1980
        self.screen_height = 1080

        # Настройки корабля:
        self.ship_limit = 3

        # Настройки пули:
        self.bullet_width = 5
        self.bullet_height = 30
        self.bullet_color = (229, 144, 97)
        self.bullets_allowed = 3  # Ограничим количество снарядов.

        self.speedup_scale = 1.1  # Темп ускорения игры.
        self.score_scale = 1.5  # Темп увеличения получения очков за убитого пришельца.

        self.hard_level = 10
        self.medium_level = 5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализация динамических настроек игры."""
        self.ship_speed_factor = 4  # Скорость движения корабля.
        self.bullet_speed_factor = 3  # Скорость движения пули.
        self.alien_speed_factor = 1  # Скорость движения пришельцев.
        self.fleet_drop_speed_factor = 30  # Скорость снижения пришельцев.
        self.fleet_direction = 1  # "1" для движения вправо, "-1" для движения влево
        self.alien_points = 10

    def increase_game(self):
        """Увеличивает скорость в игре."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.fleet_drop_speed_factor += 1
        self.alien_points = int(self.alien_points * self.score_scale)  # "int" чтобы кол-во очков было целым числом.

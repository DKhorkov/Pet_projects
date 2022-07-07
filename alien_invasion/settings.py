"""Класс настроек игры."""


class Settings:
    """Класс для настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализация настроек игры."""
        # Настройки экрана:
        self.bg_color = 'blue'
        self.screen_width = 1980
        self.screen_height = 1080

        # Настройки корабля:
        self.ship_speed = 4

        # Настройки пули:
        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 30
        self.bullet_color = (229, 144, 97)
        self.bullets_allowed = 4  # Ограничим количество снарядов.

        # Настройки пришельцев:
        self.alien_speed = 1
        self.fleet_drop_speed = 30  # Скорость снижения при достижении края
        self.fleet_direction = 1  # "1" для движения вправо, "-1" для движения влево

"""Класс дял ведения игровой статистики Alien Invasion."""
import json

class GameStats:
    """Игровая статистика AI."""

    def __init__(self, settings):
        """Инициализация атрибутов класса."""
        self.settings = settings
        self.reset_stats()
        self.game_active = False  # Флаг. Нужен для продолжения и окончания игры.
        with open('record.txt') as f:  # Рекорд хранится в файле.
            self.record = int(json.load(f))

    def reset_stats(self):
        """Инициализация статистики во время игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

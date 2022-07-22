class Settings:
    """Настройки для игры на двоих."""

    def __init__(self):
        """Атрибуты статических настроек."""
        self.screen_width = 1200
        self.screen_height = 900
        self.screen_color = 'black'

        self.square_face = 75
        self.square_1_color = 'blue'
        self.square_2_color = 'red'
        self.lives = 3

        self.bullet_widht = 40
        self.bullet_height = 15
        self.bullet_color = 'white'
        self.bullets_limit = 3

        self.initialize_dynamic_settings()

    def square_start_position_1(self, square):
        """Перемещение на первую исходную позицию."""
        square.rect.left = 20
        square.rect.centery = self.screen_height / 2

    def square_start_position_2(self, square):
        """Перемещение на вторую исходную позицию."""
        square.rect.right = self.screen_width - 20
        square.rect.centery = self.screen_height / 2

    def initialize_dynamic_settings(self):
        """Инициализация динамических настреок игры."""
        self.square_speed = 1
        self.bullet_speed = 2

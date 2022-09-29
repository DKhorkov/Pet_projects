class Settings:
    """Настройки для игры на двоих."""

    def __init__(self):
        """Атрибуты статических настроек."""
        self.screen_width = 1200
        self.screen_height = 900
        self.screen_color = 'black'

        self.network_server = ""
        self.network_port = 5555

        self.square_face = 75
        self.square_1_color = 'green'
        self.square_1_x = 20
        self.square_1_y = self.screen_height / 2
        self.square_2_x = self.screen_width - 20 - self.square_face
        self.square_2_y = self.screen_height / 2
        self.square_2_color = 'red'
        self.lives = 3

        self.bullet_widht = 40
        self.bullet_height = 15
        self.bullet_color = 'white'
        self.bullets_limit = 1

        self.square_speed = 10
        self.bullet_speed = 20

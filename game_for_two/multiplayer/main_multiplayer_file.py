import pygame
from pygame import font
from pygame.sprite import Group

from network import Network
from settings import Settings
from lives import Lives


class MultiplayerGame:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Multiplayer client")

        self.network = Network(self.settings.network_server, self.settings.network_port)
        self.player_1 = self.network.get_player()
        self.player_2 = self.network.send(self.player_1)

        self.game_active = True
        self.clock = pygame.time.Clock()

        self.font = font.SysFont(None, 30)

    def redraw_window(self, player, player_2):
        self.screen.fill(self.settings.screen_color)
        player.draw_rect(self.screen)
        self.draw_player1_lives(self.screen, self.font, "YOUR LIVES:", player)
        for bullet in player.bullets:
            bullet.draw_bullet(self.screen)
        player_2.draw_rect(self.screen)
        self.draw_player2_lives(self.screen, self.font, "ENEMY'S LIVES:", player_2)
        for bullet in player_2.bullets:
            bullet.draw_bullet(self.screen)
        pygame.display.update()

    def _check_collision(self):
        """Проверка столкновения объектов."""
        # ССтолкновение пуль:
        pygame.sprite.groupcollide(self.player_1.bullets, self.player_2.bullets, True, True)
        collision = pygame.sprite.spritecollideany(self.player_1, self.player_2.bullets)
        if collision:
            self.player_1.bullets.empty()
            self.player_2.bullets.empty()
            self.player_1.lives -= 1
            self.player_1.start_pos()

    def draw_player1_lives(self, screen, font, text, player):
        """Рисует жизни первого квадрата."""
        self.lives_str = text
        self.lives_image = font.render(self.lives_str, True, 'white', 'black')

        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = 20
        self.lives_rect.top = 20

        self.player_lives = Group()
        for live_number in range(player.lives):
            live = Lives(screen)
            live.rect.x = self.lives_rect.right + live_number * (live.rect.width + 15)
            live.rect.y = 0
            self.player_lives.add(live)

        screen.blit(self.lives_image, self.lives_rect)
        self.player_lives.draw(screen)

    def draw_player2_lives(self, screen, font, text, player):
        """Рисует жизни первого квадрата."""
        self.lives_str = text
        self.screen_rect = screen.get_rect()
        self.lives_image = font.render(self.lives_str, True, 'white', 'black')

        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.right = self.screen_rect.right - 200
        self.lives_rect.top = 20

        self.player_lives = Group()
        for live_number in range(player.lives):
            live = Lives(screen)
            live.rect.x = self.lives_rect.right + live_number * (live.rect.width + 15)
            live.rect.y = 0
            self.player_lives.add(live)

        screen.blit(self.lives_image, self.lives_rect)
        self.player_lives.draw(screen)

    def check_lives(self):
        if self.player_1.lives <= 0 or self.player_2.lives <= 0:
            self.game_active = False

    def run_client(self):
        while self.game_active:
            self.clock.tick(60)
            self.check_lives()
            self._check_collision()
            self.player_2 = self.network.send(self.player_1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_active = False
            self.player_1.move()
            self.redraw_window(self.player_1, self.player_2)
            pygame.display.flip()


if __name__ == "__main__":
    game = MultiplayerGame()
    game.run_client()

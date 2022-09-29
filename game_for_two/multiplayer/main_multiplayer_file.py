import pygame

from network import Network
from settings import Settings


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

    def redraw_window(self, player, player_2):
        self.screen.fill(self.settings.screen_color)
        player.draw_rect(self.screen)
        for bullet in player.bullets:
            bullet.draw_bullet(self.screen)
        player_2.draw_rect(self.screen)
        for bullet in player_2.bullets:
            bullet.draw_bullet(self.screen)
        pygame.display.update()

    def run_client(self):
        while self.game_active:
            self.clock.tick(60)
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

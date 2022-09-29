import pygame

from settings import Settings
from bullet import Bullet


class Player1:

    def __init__(self, x, y, square_face, square_color):
        self.settings = Settings()
        self.x = x
        self.y = y
        self.width = square_face
        self.height = square_face
        self.color = square_color
        self.bullets = pygame.sprite.Group()

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw_rect(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self.y > 20:
                self.y -= self.settings.square_speed
        elif keys[pygame.K_s]:
            if self.y < (self.settings.screen_height - self.settings.square_face - 20):
                self.y += self.settings.square_speed
        elif keys[pygame.K_SPACE]:
            if len(self.bullets) < self.settings.bullets_limit:
                new_bullet = Bullet(self.settings)
                new_bullet.bullet_start_position_1(self.rect)
                self.bullets.add(new_bullet)

        self.update_position()

    def update_position(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.check_bullets()

    def start_pos(self):
        self.x = self.settings.square_1_x
        self.y = self.settings.square_1_y

    def check_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.update_bullet_position_1()
            if bullet.rect.right > (self.settings.screen_width - 20):
                self.bullets.remove(bullet)


class Player2(Player1):

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            if self.y > 20:
                self.y -= self.settings.square_speed
        elif keys[pygame.K_s]:
            if self.y < (self.settings.screen_height - self.settings.square_face - 20):
                self.y += self.settings.square_speed
        elif keys[pygame.K_SPACE]:
            if len(self.bullets) < self.settings.bullets_limit:
                new_bullet = Bullet(self.settings)
                new_bullet.bullet_start_position_2(self.rect)
                self.bullets.add(new_bullet)

        self.update_position()

    def check_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.update_bullet_position_2()
            if bullet.rect.left < 20:
                self.bullets.remove(bullet)

    def start_pos(self):
        self.x = self.settings.square_2_x
        self.y = self.settings.square_2_y


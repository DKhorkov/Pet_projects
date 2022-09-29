import pygame

from settings import Settings


class Player:

    def __init__(self, x, y, square_face, square_color):
        self.x = x
        self.y = y
        self.width = square_face
        self.height = square_face
        self.color = square_color
        self.rect = (self.x, self.y, self.width, self.height)

    def draw_rect(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= 1
        elif keys[pygame.K_s]:
            self.y += 1
        self.update_position()

    def update_position(self):
        self.rect = (self.x, self.y, self.width, self.height)

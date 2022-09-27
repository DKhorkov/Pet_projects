import pygame
from network import Network

vel = 1
pygame.init()
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Test")

client_number = 0


class Player:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (self.x, self.y, self.width, self.height)

    def draw_rect(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.y -= vel
        elif keys[pygame.K_s]:
            self.y += vel
        elif keys[pygame.K_a]:
            self.x -= vel
        elif keys[pygame.K_d]:
            self.x += vel
        self.update_position()

    def update_position(self):
        self.rect = (self.x, self.y, self.width, self.height)


def redraw_window(win, player, player_2):
    win.fill((255, 255, 255))
    player.draw_rect(win)
    player_2.draw_rect(win)
    pygame.display.update()


def read_pos(string):
    """Поскольку отправялем на сервер строки, необходимо их обработать для изменения позиции квадрата"""
    strn = string.split(",")
    return int(strn[0]), int(strn[1])


def make_pos(tup):
    """Для отправки инфы на сервер, необходимо преобразовать ее в строку"""
    return str(tup[0]) + "," + str(tup[1])


def main():
    run = True
    network = Network("192.168.0.111", 5555)
    start_pos = read_pos(network.get_pos())  # получаем позицию игрока (первый или второй)
    p = Player(start_pos[0], start_pos[1], 50, 50, 'green')
    p2 = Player(0, 0, 50, 50, 'red')
    while run:
        p2_pos = read_pos(network.send(make_pos((p.x, p.y))))  # Передаем серверу позицию в виде строки и читаем ее
        p2.x = p2_pos[0]
        p2.y = p2_pos[1]
        p2.update_position()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        p.move()
        redraw_window(win, p, p2)
        pygame.display.flip()


main()
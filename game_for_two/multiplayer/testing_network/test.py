import pygame

from network import Network


pygame.init()
win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Test")


def redraw_window(win, player, player_2):
    win.fill((255, 255, 255))
    player.draw_rect(win)
    player_2.draw_rect(win)
    pygame.display.update()


def main():
    run = True
    network = Network("", 5555)
    clock = pygame.time.Clock()
    p1 = network.get_player()
    while run:
        clock.tick(60)
        p2 = network.send(p1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        p1.move()
        redraw_window(win, p1, p2)
        pygame.display.flip()


main()
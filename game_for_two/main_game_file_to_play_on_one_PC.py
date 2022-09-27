# Игра с квадратами для двоих.
import pygame
from pygame.sprite import Group
from time import sleep

from settings import Settings
from square import Square
from bullet import Bullet
from scoreboard import Scoreboard
from button import Button


class GameForTwo:
    """Класс для запуска игры."""

    def __init__(self):
        """Атрибуты игры."""
        pygame.init()

        # Создание экрана:
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Square game for two')

        self._create_squares()  # Создание квадратов.
        self._create_moving_flags()  # Создание флагов движения.

        self.first_square_bullets = pygame.sprite.Group()
        self.second_square_bullets = pygame.sprite.Group()

        self.scoreboard = Scoreboard(self.screen, self.settings, self.first_square, self.second_square)

        self.game_active = False
        self.play_button = Button(self.screen, 'PLAY')

    def _check_play_button(self, mouse_position):
        """Проверка нажатия мышкой"""
        button_clocked = self.play_button.rect.collidepoint(mouse_position)

        if button_clocked and not self.game_active:
            self.game_active = True
            self._reset_stats()

    def _create_moving_flags(self):
        """Создание флагов для движения квадратов."""
        self.first_square_moving_up = False
        self.second_square_moving_up = False
        self.first_square_moving_down = False
        self.second_square_moving_down = False

    def _create_squares(self):
        """Создание квадратов для управления игроками."""
        self.first_square = Square(self.screen, self.settings, self.settings.square_1_color)
        self.settings.square_start_position_1(self.first_square)

        self.second_square = Square(self.screen, self.settings, self.settings.square_2_color)
        self.settings.square_start_position_2(self.second_square)

    def _check_keydown_events(self, event):
        """Проверка событий при нажатии клавиш клавиатуры."""
        if event.key == pygame.K_w:
            self.first_square_moving_up = True
        elif event.key == pygame.K_s:
            self.first_square_moving_down = True
        elif event.key == pygame.K_UP:
            self.second_square_moving_up = True
        elif event.key == pygame.K_DOWN:
            self.second_square_moving_down = True
        elif event.key == pygame.K_f:
            if len(self.first_square_bullets) < self.settings.bullets_limit:
                new_bullet = Bullet(self.screen, self.settings)
                new_bullet.bullet_start_position_1(self.first_square)
                self.first_square_bullets.add(new_bullet)
        elif event.key == pygame.K_KP0:
            if len(self.second_square_bullets) < self.settings.bullets_limit:
                new_bullet = Bullet(self.screen, self.settings)
                new_bullet.bullet_start_position_2(self.second_square)
                self.second_square_bullets.add(new_bullet)
        elif event.key == pygame.K_p and not self.game_active:
            self._reset_stats()

    def _reset_stats(self):
        """Обновление жизней при начале игры."""
        sleep(1)
        self.game_active = True
        self.scoreboard.first_square.lives = self.settings.lives
        self.scoreboard.second_square.lives = self.settings.lives
        self.scoreboard.draw_first_square_lives()
        self.scoreboard.draw_second_square_lives()
        self.settings.square_start_position_1(self.first_square)
        self.settings.square_start_position_2(self.second_square)

    def _check_keyup_events(self, event):
        """Проверка событий при отпускании клавиш клавиатуры."""
        if event.key == pygame.K_w:
            self.first_square_moving_up = False
        elif event.key == pygame.K_s:
            self.first_square_moving_down = False
        elif event.key == pygame.K_UP:
            self.second_square_moving_up = False
        elif event.key == pygame.K_DOWN:
            self.second_square_moving_down = False

    def _check_events(self):
        """Проверка событий, влияющих на игру."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                self._check_play_button(mouse_position)

    def _update_bullets(self):
        """Обновляет пули."""
        for bullet in self.first_square_bullets:
            bullet.update_bullet_position_1()
            if bullet.rect.right > self.second_square.rect.right:
                self.first_square_bullets.remove(bullet)
            bullet.draw_bullet()
        for bullet in self.second_square_bullets:
            bullet.update_bullet_position_2()
            if bullet.rect.left < self.first_square.rect.left:
                self.second_square_bullets.remove(bullet)
            bullet.draw_bullet()

    def _check_collision(self):
        """Проверка столкновения объектов."""
        # ССтолкновение пуль:
        pygame.sprite.groupcollide(self.first_square_bullets, self.second_square_bullets, True, True)

        # Столкновение пули с квадратом:
        square_1_collision = pygame.sprite.spritecollideany(self.first_square, self.second_square_bullets)
        square_2_collision = pygame.sprite.spritecollideany(self.second_square, self.first_square_bullets)
        if square_1_collision:
            sleep(0.5)
            self.first_square_bullets.empty()
            self.second_square_bullets.empty()
            self.settings.square_start_position_1(self.first_square)
            self.scoreboard.first_square.lives -= 1
            self.scoreboard.draw_first_square_lives()
        elif square_2_collision:
            sleep(0.5)
            self.first_square_bullets.empty()
            self.second_square_bullets.empty()
            self.settings.square_start_position_2(self.second_square)
            self.scoreboard.second_square.lives -= 1
            self.scoreboard.draw_second_square_lives()

    def _update_squares(self):
        """Обновляет квадраты на экране."""
        self.first_square.square_moving(self.first_square_moving_up, self.first_square_moving_down)
        self.first_square.draw_square()
        self.second_square.square_moving(self.second_square_moving_up, self.second_square_moving_down)
        self.second_square.draw_square()

    def _check_lives(self):
        """Проверка, что жизни обоих игроков больше нуля."""
        if self.scoreboard.first_square.lives <= 0 or self.scoreboard.second_square.lives <= 0:
            self.game_active = False

    def run_game(self):
        """Запуск игры."""
        while True:
            self.screen.fill(self.settings.screen_color)
            if not self.game_active:
                self.play_button.draw_button()
            self._check_lives()
            self._check_events()

            if self.game_active:
                self.scoreboard.show_lives()

                self._update_squares()  # Обновляет квадраты на экране.
                self._update_bullets()  # Обновляет пули на экране.
                self._check_collision()

            pygame.display.flip()


if __name__ == '__main__':
    game = GameForTwo()
    game.run_game()

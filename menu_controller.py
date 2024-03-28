import pygame
import sys
from os.path import join
from my_car import get_car_image
from globals import Globals
from game_controller import GameController
from button import ButtonImage


def initialize_game():
    pygame.init()
    scr = pygame.display.set_mode((Globals.WIDTH, Globals.HEIGHT))
    pygame.display.set_caption("Car Racer")
    return scr


def chooser_wheel(index: int, step: int, array_length: int) -> int:
    return (index + step) % array_length


class MenuController:
    def __init__(self):
        # Створюємо кнопки
        self.play_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 2, 300, 130,
                                       join('images', 'buttons', 'button_play.png'))
        self.set_button = ButtonImage(Globals.WIDTH / 2 - 75, Globals.HEIGHT / 3 * 2, 100, 100,
                                      join('images', 'buttons', 'button_settings.png'))
        self.exit_button = ButtonImage(Globals.WIDTH / 2 + 75, Globals.HEIGHT / 3 * 2, 95, 95,
                                       join('images', 'buttons', 'button_exit.png'))

        self.resol_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 2, 300, 120,
                                        join('images', 'buttons', 'button_resolution.png'))
        self.back_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 10 * 9, 200, 100,
                                       join('images', 'buttons', 'button_back.png'))

        self.small_res_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 2, 325, 145,
                                            join('images', 'buttons', 'small_resol_button.png'))
        self.medium_res_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 3, 295, 105,
                                             join('images', 'buttons', 'medium_resol_button.png'))
        self.big_res_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 4, 280, 135,
                                          join('images', 'buttons', 'big_resol_button.png'))

        # Створюємо фон
        self.background = pygame.image.load(join('images', 'backgrounds', 'car_background.jpg'))
        self.set_background = pygame.image.load(join('images', 'backgrounds', 'set_background.jpg'))

    def main_flow(self):
        run = True
        screen = initialize_game()
        while run:
            self.__open_main_menu(screen)

    def __open_main_menu(self, screen):
        run = True
        while run:
            screen.fill((0, 0, 0))  # Заповнюємо чорним кольором
            screen.blit(self.background, (0, -80))
            menu_font = pygame.font.Font(None, 70)
            text_surf = menu_font.render("RACER", True, (0, 255, 255))
            text_rect = text_surf.get_rect(center=(Globals.WIDTH / 2, Globals.HEIGHT / 3))
            screen.blit(text_surf, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Реалізація кнопки вийти
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_button.is_clicked(event.pos):
                        pygame.quit()
                        sys.exit()

                # Реалізація кнопки відкрити налаштування
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.set_button.is_clicked(event.pos):
                        self.__setting_menu(screen)

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.play_button.is_clicked(event.pos):
                        self.__car_chooser(screen)

            for btn in [self.play_button, self.set_button, self.exit_button]:
                btn.draw(screen)

            pygame.display.flip()  # Оновлення відображення на екран

    def __setting_menu(self, screen):
        run = True
        while run:
            screen.fill((0, 0, 0))  # Заповнюємо чорним кольором
            screen.blit(self.set_background, (-50, -300))
            menu_font = pygame.font.Font(None, 70)
            text_surf = menu_font.render("Settings", True, (0, 255, 255))
            text_rect = text_surf.get_rect(center=(Globals.WIDTH / 2, Globals.HEIGHT / 3))
            screen.blit(text_surf, text_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Реалізація кнопки Back
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button.is_clicked(event.pos):
                        return

                # Реалізація кнопки Resolution
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.resol_button.is_clicked(event.pos):
                        self.__video_set_menu(screen)

            for btn in [self.back_button, self.resol_button]:
                btn.draw(screen)

            pygame.display.flip()  # Оновлення відображення на екран

    def __video_set_menu(self, screen):
        run = True
        while run:
            screen.fill((0, 0, 0))  # Заповнюємо чорним кольором
            screen.blit(self.set_background, (-50, -300))
            menu_font = pygame.font.Font(None, 70)
            text_surf = menu_font.render("Video settings", True, (0, 255, 255))
            text_rect = text_surf.get_rect(center=(Globals.WIDTH / 2, Globals.HEIGHT / 6))
            screen.blit(text_surf, text_rect)

            for btn in [self.back_button, self.small_res_button, self.medium_res_button, self.big_res_button]:
                btn.draw(screen)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.back_button.is_clicked(event.pos):
                            return

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.small_res_button.is_clicked(event.pos):
                            Globals.WIDTH, Globals.HEIGHT = 800, 600
                            screen = self.__button_pos_update()
                            self.background = pygame.image.load(join('images', 'backgrounds', 'car_background_small.jpg'))
                            self.set_background = pygame.image.load(
                                join('images', 'backgrounds', 'set_background_small.jpg'))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.medium_res_button.is_clicked(event.pos):
                            Globals.WIDTH, Globals.HEIGHT = 1024, 768
                            screen = self.__button_pos_update()
                            self.background = pygame.image.load(join('images', 'backgrounds', 'car_background_medium.jpg'))
                            self.set_background = pygame.image.load(
                                join('images', 'backgrounds', 'set_background_medium.jpg'))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.big_res_button.is_clicked(event.pos):
                            Globals.WIDTH, Globals.HEIGHT = 1200, 800
                            screen = self.__button_pos_update()
                            self.background = pygame.image.load(join('images', 'backgrounds', 'car_background.jpg'))
                            self.set_background = pygame.image.load(join('images', 'backgrounds', 'set_background.jpg'))

            pygame.display.flip()  # Оновлення відображення на екран

    # Зміна положення кнопок при зміні масштабу
    def __button_pos_update(self):
        screen = pygame.display.set_mode((Globals.WIDTH, Globals.HEIGHT))
        self.resol_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 2)
        self.play_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 2)
        self.set_button.set_pos(Globals.WIDTH / 2 - 75, Globals.HEIGHT / 3 * 2)
        self.exit_button.set_pos(Globals.WIDTH / 2 + 75, Globals.HEIGHT / 3 * 2)
        self.back_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 10 * 9)
        self.small_res_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 2)
        self.medium_res_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 3)
        self.big_res_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 4)
        return screen

    def __car_chooser(self, screen):
        # Завантажуємо задній фон
        choose_car_background = pygame.image.load(join('images', 'backgrounds', 'choose_car_background.jpg'))
        choose_car_background = pygame.transform.scale(choose_car_background, (Globals.WIDTH, Globals.HEIGHT))

        path_arrow = join('images', 'buttons', 'arrow_left.png')
        arrow_left = ButtonImage(Globals.WIDTH * 0.25, Globals.HEIGHT * 0.5, 100, 100, path_arrow)
        arrow_right = ButtonImage(Globals.WIDTH * 0.75, Globals.HEIGHT * 0.5, 100, 100, path_arrow)
        arrow_right.image = pygame.transform.flip(arrow_left.image, True, False)

        second_play_button = ButtonImage(Globals.WIDTH * 0.5, Globals.HEIGHT * 0.7, 100, 100,
                                         join('images', 'buttons', 'button_second_play.png'))

        angle = 0
        clock = pygame.time.Clock()
        run = True
        index = 0
        car = Globals.CAR_CONTAINER[index]

        menu_font = pygame.font.Font(None, 70)
        text_surf = menu_font.render(car.name, True, (0, 255, 255))
        text_rect = text_surf.get_rect(center=(Globals.WIDTH / 2, Globals.HEIGHT / 3))
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.back_button.is_clicked(event.pos):
                        run = False
                    if second_play_button.is_clicked(event.pos):
                        GameController.game_start(screen, car)
                    if arrow_left.is_clicked(event.pos):
                        index = chooser_wheel(index, -1, len(Globals.CAR_CONTAINER))
                    if arrow_right.is_clicked(event.pos):
                        index = chooser_wheel(index, 1, len(Globals.CAR_CONTAINER))
                    car = Globals.CAR_CONTAINER[index]
                    text_surf = menu_font.render(car.name, True, (0, 255, 255))
                    text_rect = text_surf.get_rect(center=(Globals.WIDTH / 2, Globals.HEIGHT / 3))

            screen.blit(choose_car_background, (0, 0))

            rotate_image = pygame.transform.rotate(get_car_image(car.image, car.size), angle - 90)
            rect = rotate_image.get_rect(center=(Globals.WIDTH * 0.5, Globals.HEIGHT * 0.5))
            angle = (angle + 1) % 360

            for btn in [arrow_left, arrow_right, self.back_button, second_play_button]:
                btn.draw(screen)

            screen.blit(rotate_image, rect)
            screen.blit(text_surf, text_rect)

            pygame.display.flip()
            clock.tick(60)

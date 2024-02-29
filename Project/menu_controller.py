import os

import pygame
import sys

from my_car import get_car_image
from globals import Globals
from game_controller import GameController
from button import ButtonImage

pygame.init()

#clock = pygame.time.Clock()
# Константи вже встановлені у файлі globals, ще раз встановлювати значення не треба
# Globals.WIDTH = 1200 
# Globals.HEIGHT = 800
screen = pygame.display.set_mode((Globals.WIDTH, Globals.HEIGHT))
pygame.display.set_caption("Car Racer")
background = pygame.image.load('images/car_background.jpg')

# Створюємо кнопки
play_button = ButtonImage(Globals.WIDTH / 2 - (300 / 2), 300, 300, 130, 'images/button_play.png')
set_button = ButtonImage(Globals.WIDTH / 2 - (260 / 2), 420, 100, 100, 'images/button_settings.png')
exit_button = ButtonImage(Globals.WIDTH / 2 + 27, 420, 95, 95, 'images/button_exit.png')

# menu_main пуеназвав на open_main_menu
def open_main_menu():
    run = True
    while run:
        screen.fill((0, 0, 0)) #Заповнюємо чорним кольором
        screen.blit(background, (0, -80))
        menu_font = pygame.font.Font(None, 70)
        text_surf = menu_font.render("CAR VS TIME RACER", True, (0, 255, 255))
        text_rect = text_surf.get_rect(center=(Globals.WIDTH / 2, 200))
        screen.blit(text_surf, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Реалізація кнопки вийти
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.is_clicked(event.pos):
                    pygame.quit()
                    sys.exit()

            # Реалізація кнопки відкрити налаштування
            if event.type == pygame.MOUSEBUTTONDOWN:
                if set_button.is_clicked(event.pos):
                    setting_menu()

            if event.type == pygame.MOUSEBUTTONUP:
                if play_button.is_clicked(event.pos):
                    car_chooser()
                    # GameController.game_start(screen)

        for btn in [play_button, set_button, exit_button]:
            btn.draw(screen)

        pygame.display.flip()  #Оновлення відображення на екран


def setting_menu():
    global background, play_button, set_button, exit_button  #Оголошуємо фон і кнопки як глобальну змінну

    set_background = pygame.image.load('images/set_background.jpg')
    resol_button = ButtonImage(Globals.WIDTH / 2 - (300 / 2), 250, 300, 120, 'images/button_resolution.png')
    back_button = ButtonImage(Globals.WIDTH / 2 - (194 / 2), 400, 200, 100, 'images/button_back.png')
    resolution_options = [(800, 600), (1024, 768), (1200, 800)]
    current_resolution_index = 0

    run = True
    while run:
        screen.fill((0, 0, 0))  #Заповнюємо чорним кольором
        screen.blit(set_background, (-50, -300))
        menu_font = pygame.font.Font(None, 70)
        text_surf = menu_font.render("Settings", True, (0, 255, 255))
        text_rect = text_surf.get_rect(center=(Globals.WIDTH / 2, 200))
        screen.blit(text_surf, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    run = False

            # Реалізація кнопки Resolution
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resol_button.is_clicked(event.pos):
                    current_resolution_index = (current_resolution_index + 1) % len(resolution_options)
                    new_resolution = resolution_options[current_resolution_index]  # Отримуємо нове розширення на основі оновленого індексу
                    Globals.WIDTH, Globals.HEIGHT = new_resolution
                    pygame.display.set_mode((Globals.WIDTH, Globals.HEIGHT))

                    # Змінюємо фонове зображення відповідно до індексу
                    if current_resolution_index == 0:
                        resol_button.set_pos(Globals.WIDTH / 2 - (250 / 2), 250)
                        back_button.set_pos(Globals.WIDTH / 2 - (150 / 2), 375)
                        play_button.set_pos(Globals.WIDTH / 2 - (300 / 2), 300)
                        set_button.set_pos(Globals.WIDTH / 2 - (260 / 2), 420)
                        exit_button.set_pos(Globals.WIDTH / 2 + 27, 420)
                        background = pygame.image.load('images/car_background_small.jpg')
                        set_background = pygame.image.load('images/set_background_small.jpg')

                    elif current_resolution_index == 1:
                        resol_button.set_pos(Globals.WIDTH / 2 - (300 / 2), 250)
                        back_button.set_pos(Globals.WIDTH / 2 - (194 / 2), 400)
                        play_button.set_pos(Globals.WIDTH / 2 - (300 / 2), 300)
                        set_button.set_pos(Globals.WIDTH / 2 - (260 / 2), 420)
                        exit_button.set_pos(Globals.WIDTH / 2 + 27, 420)
                        background = pygame.image.load('images/car_background_medium.jpg')
                        set_background = pygame.image.load('images/set_background_medium.jpg')

                    elif current_resolution_index == 2:
                        resol_button.set_pos(Globals.WIDTH / 2 - (300 / 2), 250)
                        back_button.set_pos(Globals.WIDTH / 2 - (194 / 2), 400)
                        play_button.set_pos(Globals.WIDTH / 2 - (300 / 2), 300)
                        set_button.set_pos(Globals.WIDTH / 2 - (260 / 2), 420)
                        exit_button.set_pos(Globals.WIDTH / 2 + 27, 420)
                        background = pygame.image.load('images/car_background.jpg')
                        set_background = pygame.image.load('images/set_background.jpg')

                    screen.blit(background, (0, -80))

        for btn in [back_button, resol_button]:
            btn.draw(screen)

        pygame.display.flip() #Оновлення відображення на екран


def car_chooser():
    path_arrow = os.path.join('images', 'arrow_left.png')
    arrow_left = ButtonImage(Globals.WIDTH * 0.25, Globals.HEIGHT * 0.5, 100, 100, path_arrow)
    arrow_right = ButtonImage(Globals.WIDTH * 0.75, Globals.HEIGHT * 0.5, 100, 100, path_arrow)
    arrow_right.image = pygame.transform.flip(arrow_left.image, True, False)

    angle = 0
    clock = pygame.time.Clock()
    run = True
    index = 0
    car = Globals.CAR_CONTAINER[index]
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if arrow_left.is_clicked(event.pos):
                    index = (index - 1) % len(Globals.CAR_CONTAINER)
                    car = Globals.CAR_CONTAINER[index]
                if arrow_right.is_clicked(event.pos):
                    index = (index + 1) % len(Globals.CAR_CONTAINER)
                    car = Globals.CAR_CONTAINER[index]

        screen.fill(Globals.BG_COLOR)
        rotate_image = pygame.transform.rotate(get_car_image(car.image, (50, 60)), angle - 90)
        rect = rotate_image.get_rect(center=(Globals.WIDTH*0.5, Globals.HEIGHT*0.5))
        angle = (angle + 1) % 360

        arrow_left.draw(screen)
        arrow_right.draw(screen)

        screen.blit(rotate_image, rect)

        pygame.display.flip()
        clock.tick(60)


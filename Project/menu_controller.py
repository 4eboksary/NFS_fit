import pygame
import sys
from os.path import join
from my_car import get_car_image
from globals import Globals
from game_controller import GameController
from button import ButtonImage

pygame.init()
# clock = pygame.time.Clock()
# Константи вже встановлені у файлі globals, ще раз встановлювати значення не треба
# Globals.WIDTH = 1200 
# Globals.HEIGHT = 800
screen = pygame.display.set_mode((Globals.WIDTH, Globals.HEIGHT))
pygame.display.set_caption("Car Racer")

# Створюємо кнопки
play_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 2, 300, 130, join('images', 'buttons', 'button_play.png'))
set_button = ButtonImage(Globals.WIDTH / 2 - 75, Globals.HEIGHT / 3 * 2, 100, 100,join('images', 'buttons', 'button_settings.png'))
exit_button = ButtonImage(Globals.WIDTH / 2 + 75, Globals.HEIGHT / 3 * 2, 95, 95,join('images', 'buttons', 'button_exit.png'))

resol_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 2, 300, 120,join('images', 'buttons', 'button_resolution.png'))
back_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 10 * 9, 200, 100,join('images', 'buttons', 'button_back.png'))

small_res_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 2, 325, 145,join('images', 'buttons', 'small_resol_button.png'))
medium_res_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 3, 295, 105,join('images', 'buttons', 'medium_resol_button.png'))
big_res_button = ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 4, 280, 135,join('images', 'buttons', 'big_resol_button.png'))

# Створюємо фон
background = pygame.image.load(join('images', 'backgrounds', 'car_background.jpg'))
set_background = pygame.image.load(join('images', 'backgrounds', 'set_background.jpg'))

def open_main_menu():
    run = True
    while run:
        screen.fill((0, 0, 0))  # Заповнюємо чорним кольором
        screen.blit(background, (0, -80))
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

        for btn in [play_button, set_button, exit_button]:
            btn.draw(screen)

        pygame.display.flip()  # Оновлення відображення на екран


def setting_menu():
    run = True
    while run:
        screen.fill((0, 0, 0))  # Заповнюємо чорним кольором
        screen.blit(set_background, (-50, -300))
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
                if back_button.is_clicked(event.pos):
                    run = False

            # Реалізація кнопки Resolution
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resol_button.is_clicked(event.pos):
                    video_set_menu()

        for btn in [back_button, resol_button]:
            btn.draw(screen)

        pygame.display.flip()  # Оновлення відображення на екран


def video_set_menu():
    # Оголошуємо фон як глобальну змінну
    global background, set_background
    run = True
    while run:
        screen.fill((0, 0, 0))  # Заповнюємо чорним кольором
        screen.blit(set_background, (-50, -300))
        menu_font = pygame.font.Font(None, 70)
        text_surf = menu_font.render("Video settings", True, (0, 255, 255))
        text_rect = text_surf.get_rect(center=(Globals.WIDTH / 2, Globals.HEIGHT / 6))
        screen.blit(text_surf, text_rect)

        for btn in [back_button, small_res_button, medium_res_button, big_res_button]:
            btn.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.is_clicked(event.pos):
                        run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if small_res_button.is_clicked(event.pos):
                        Globals.WIDTH, Globals.HEIGHT = 800, 600
                        button_pos_update()
                        #background = pygame.image.load(join('images', 'backgrounds', 'car_background_small.jpg'))
                        #set_background = pygame.image.load(join('images', 'backgrounds', 'set_background_small.jpg'))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if medium_res_button.is_clicked(event.pos):
                        Globals.WIDTH, Globals.HEIGHT = 1024, 768
                        button_pos_update()
                        background = pygame.image.load(join('images', 'backgrounds', 'car_background_medium.jpg'))
                        set_background = pygame.image.load(join('images', 'backgrounds', 'set_background_medium.jpg'))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if big_res_button.is_clicked(event.pos):
                        Globals.WIDTH, Globals.HEIGHT = 1200, 800
                        button_pos_update()
                        background = pygame.image.load(join('images', 'backgrounds', 'car_background.jpg'))
                        set_background = pygame.image.load(join('images', 'backgrounds', 'set_background.jpg'))

        pygame.display.flip()  # Оновлення відображення на екран


# Зміна положення кнопок при зміні масштабу
def button_pos_update():
    pygame.display.set_mode((Globals.WIDTH, Globals.HEIGHT))
    resol_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 2)
    play_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 2)
    set_button.set_pos(Globals.WIDTH / 2 - 75, Globals.HEIGHT / 3 * 2)
    exit_button.set_pos(Globals.WIDTH / 2 + 75, Globals.HEIGHT / 3 * 2)
    back_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 10 * 9)
    small_res_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 2)
    medium_res_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 3)
    big_res_button.set_pos(Globals.WIDTH / 2, Globals.HEIGHT / 7 * 4)


def car_chooser():

    #Завантажуємо задній фон
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

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                if arrow_left.is_clicked(event.pos):
                    index = (index - 1) % len(Globals.CAR_CONTAINER)
                    car = Globals.CAR_CONTAINER[index]
                if arrow_right.is_clicked(event.pos):
                    index = (index + 1) % len(Globals.CAR_CONTAINER)
                    car = Globals.CAR_CONTAINER[index]
                if back_button.is_clicked(event.pos):
                    run = False
                if second_play_button.is_clicked(event.pos):
                    GameController.game_start(screen, car)

        screen.blit(choose_car_background, (0, 0))

        rotate_image = pygame.transform.rotate(get_car_image(car.image, car.size), angle - 90)
        rect = rotate_image.get_rect(center=(Globals.WIDTH * 0.5, Globals.HEIGHT * 0.5))
        angle = (angle + 1) % 360

        for btn in [arrow_left, arrow_right, back_button, second_play_button]:
            btn.draw(screen)

        screen.blit(rotate_image, rect)

        pygame.display.flip()
        clock.tick(60)


import pygame
import sys

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

#Створюємо кнопки
play_button = ButtonImage(Globals.WIDTH / 2 - (300 / 2), 300, 300, 130, 'images/button_play.png')
set_button = ButtonImage(Globals.WIDTH / 2 - (260 / 2), 420, 100, 100, 'images/button_settings.png')
exit_button = ButtonImage(Globals.WIDTH / 2 + 27, 420, 95, 95, 'images/button_exit.png')

resol_button = ButtonImage(Globals.WIDTH / 2 - (300 / 2), 250, 300, 120, 'images/button_resolution.png')
back_button = ButtonImage(Globals.WIDTH / 2 - (200 / 2), 475, 200, 100, 'images/button_back.png')

small_res_button = ButtonImage(Globals.WIDTH / 2 - (325 / 2), 125, 325, 145, 'images/small_resol_button.png')
medium_res_button = ButtonImage(Globals.WIDTH / 2 - (295 / 2), 250, 295, 105, 'images/medium_resol_button.png')
big_res_button = ButtonImage(Globals.WIDTH / 2 - (280 / 2), 340, 280, 135, 'images/big_resol_button.png')

#Створюємо фон
background = pygame.image.load('images/car_background.jpg')
set_background = pygame.image.load('images/set_background.jpg')

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
                    GameController.game_start(screen)

        for btn in [play_button, set_button, exit_button]:
            btn.draw(screen)

        pygame.display.flip()  #Оновлення відображення на екран


def setting_menu():
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

            #Реалізація кнопки Back
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    run = False

            # Реалізація кнопки Resolution
            if event.type == pygame.MOUSEBUTTONDOWN:
                if resol_button.is_clicked(event.pos):
                   video_set_menu()

        for btn in [back_button, resol_button]:
            btn.draw(screen)

        pygame.display.flip() #Оновлення відображення на екран

def video_set_menu():
    # Оголошуємо фон і кнопки як глобальну змінну
    global background, play_button, set_button, exit_button, resol_button, set_background, back_button, small_res_button, medium_res_button, big_res_button

    run = True
    while run:
        screen.fill((0, 0, 0))  # Заповнюємо чорним кольором
        screen.blit(set_background, (-50, -300))
        menu_font = pygame.font.Font(None, 70)
        text_surf = menu_font.render("Video settings", True, (0, 255, 255))
        text_rect = text_surf.get_rect(center=(Globals.WIDTH / 2, 100))
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
                        background = pygame.image.load('images/car_background_small.jpg')
                        set_background = pygame.image.load('images/set_background_small.jpg')

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if medium_res_button.is_clicked(event.pos):
                        Globals.WIDTH, Globals.HEIGHT = 1024, 768
                        button_pos_update()
                        background = pygame.image.load('images/car_background_medium.jpg')
                        set_background = pygame.image.load('images/set_background_medium.jpg')

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if big_res_button.is_clicked(event.pos):
                        Globals.WIDTH, Globals.HEIGHT = 1200, 800
                        button_pos_update()
                        background = pygame.image.load('images/car_background.jpg')
                        set_background = pygame.image.load('images/set_background.jpg')

        pygame.display.flip()  #Оновлення відображення на екран

#Зміна положення кнопок при зміні масштабу
def button_pos_update():
        pygame.display.set_mode((Globals.WIDTH, Globals.HEIGHT))

        resol_button.set_pos(Globals.WIDTH / 2 - (300 / 2), 250)
        play_button.set_pos(Globals.WIDTH / 2 - (300 / 2), 300)
        set_button.set_pos(Globals.WIDTH / 2 - (260 / 2), 420)
        exit_button.set_pos(Globals.WIDTH / 2 + 27, 420)
        back_button.set_pos(Globals.WIDTH / 2 - (200 / 2), 100)
        small_res_button.set_pos(Globals.WIDTH / 2 - (325 / 2), 250)
        medium_res_button.set_pos(Globals.WIDTH / 2 - (295 / 2), 250)
        big_res_button.set_pos(Globals.WIDTH / 2 - (280 / 2), 250)
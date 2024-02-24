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
background = pygame.image.load('images/car_background.jpg')

# menu_main пуеназвав на open_main_menu
def open_main_menu():
    #Створюємо кнопки
    play_button = ButtonImage(Globals.WIDTH/2-(300/2), 300, 300, 130, 'images/button_play.png')
    set_button = ButtonImage(Globals.WIDTH/2-(260/2), 420, 100, 100, 'images/button_settings.png')
    exit_button = ButtonImage(Globals.WIDTH/2+27, 420, 95, 95, 'images/button_exit.png')

    run = True
    while run:
        screen.fill((0, 0, 0)) #Заповнюємо чорним кольором
        screen.blit(background, (0, -80))
        menu_font = pygame.font.Font(None, 70)
        text_surf = menu_font.render("CAR VS TIME RACER", True, (0, 255, 255))
        text_rect = text_surf.get_rect(center=(595, 250))
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

        pygame.display.flip()  # Оновлення відображення на екран


def setting_menu():
    set_background = pygame.image.load('images/set_background.jpg')
    resol_button = ButtonImage(Globals.WIDTH/2-(300/2), 250, 300, 120, 'images/button_resolution.png')
    back_button = ButtonImage(Globals.WIDTH/2-(200/2), 400, 200, 100, 'images/button_back.png')

    run = True
    while run:
        screen.fill((0, 0, 0))  # Заповнюємо чорним кольором
        screen.blit(set_background, (-50, -300))
        menu_font = pygame.font.Font(None, 70)
        text_surf = menu_font.render("Settings", True, (0, 255, 255))
        text_rect = text_surf.get_rect(center=(595, 200))
        screen.blit(text_surf, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    run = False

        for btn in [back_button, resol_button]:
            btn.draw(screen)

        pygame.display.flip()  #Оновлення відображення на екран

# цей файл ми запескати не будемо, тільки мейнбудемо
# if __name__ == "__main__":
#     menu_main()

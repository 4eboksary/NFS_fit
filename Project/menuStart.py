import pygame
import sys
from button import ButtonImage

pygame.init()

width, height = 600, 550
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racer")
background = pygame.image.load('images/car_background.jpg')

def menu_main():
    #Створюємо кнопки
    play_button = ButtonImage(174, 170, 252, 74, 'images/button_play.png')
    set_button = ButtonImage(200, 250, 80, 80, 'images/button_settings.png')
    exit_button = ButtonImage(315, 245, 80, 80, 'images/button_exit.png')

    run = True
    while run:
        screen.fill((0, 0, 0)) #Заповнюємо чорним кольором
        screen.blit(background, (-100, -1))
        menu_font = pygame.font.Font(None, 45)
        text_surf = menu_font.render("CAR VS TIME RACER", True, (0, 0, 255))
        text_rect = text_surf.get_rect(center=(300, 150))
        screen.blit(text_surf, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            #Реалізація кнопки вийти
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.is_clicked(event.pos):
                    run = False
                    pygame.quit()
                    sys.exit()

            # Реалізація кнопки відкрити налаштування
            if event.type == pygame.MOUSEBUTTONDOWN:
                if set_button.is_clicked(event.pos):
                    setting_menu()

        for btn in [play_button, set_button, exit_button]:
            btn.draw(screen)

        pygame.display.flip()  #Оновлення відображення на екран

def setting_menu():
    set_background = pygame.image.load('images/set_background.jpg')
    back_button = ButtonImage(240, 250, 120, 70, 'images/button_back.png')
    resol_button = ButtonImage(174, 170, 252, 74, 'images/button_resolution.png')

    run = True
    while run:
        screen.fill((0, 0, 0))  # Заповнюємо чорним кольором
        screen.blit(set_background, (-112, -150))
        menu_font = pygame.font.Font(None, 45)
        text_surf = menu_font.render("Settings", True, (0, 255, 255))
        text_rect = text_surf.get_rect(center=(300, 150))
        screen.blit(text_surf, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    run = False


        for btn in [back_button, resol_button]:
            btn.draw(screen)

        pygame.display.flip()  # Оновлення відображення на екран

if __name__ == "__main__":
    menu_main()

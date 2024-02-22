import pygame
import sys
from button import button_image

pygame.init()

width, height = 1200, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racer")
background = pygame.image.load('images/car_background.jpg')

def menu_main():
    #Створюємо кнопки
    play_button = button_image(width/2-(300/2), 300, 300, 130, 'images/button_play.png')
    set_button = button_image(width/2-(260/2), 420, 100, 100, 'images/button_settings.png')
    exit_button = button_image(width/2+27, 420, 95, 95, 'images/button_exit.png')

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
    resol_button = button_image(width/2-(300/2), 250, 300, 120, 'images/button_resolution.png')
    back_button = button_image(width/2-(200/2), 400, 200, 100, 'images/button_back.png')

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
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    run = False


        for btn in [back_button, resol_button]:
            btn.draw(screen)

        pygame.display.flip()  #Оновлення відображення на екран

if __name__ == "__main__":
    menu_main()

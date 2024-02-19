import pygame
import sys
from button import ButtonImage

pygame.init()

width, height = 600, 550
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racer")
background = pygame.image.load('images/car_background.jpg')

def menu_main():

    # Створюємо кнопки
    play_button = ButtonImage(174, 170, 252, 74, 'images/button_play.png')
    set_button = ButtonImage(200, 250, 80, 80, 'images/button_settings.png')
    exit_button = ButtonImage(315, 245, 80, 80, 'images/button_exit.png')

    run = True
    while run:
        screen.fill((0, 0, 0)) #заповнюємо чорним кольором
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

        for btn in [play_button, set_button, exit_button]: #по циклу промальовуємо кожну кнопку
            btn.draw(screen)

        pygame.display.flip() #оновлення відображення на екран

def setting_menu():
    pass


if __name__ == "__main__":
    menu_main()



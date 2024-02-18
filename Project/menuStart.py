import pygame
import sys
from button import ButtonImage

pygame.init()

width, height = 600, 550
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Menu")

# Створюємо кнопки
play_button = ButtonImage(174, 170, 252, 74, 'images/button_play.png')
set_button = ButtonImage(200, 250, 80, 80, 'images/button_settings.png')
exit_button = ButtonImage(315,245,80,80,'images/button_exit.png')

def menu_main():
    run = True
    while run:
        screen.fill((0, 0, 0)) #заповнюємо чорним кольором
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        play_button.draw(screen)
        set_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip() #оновлення відображення на екран


if __name__ == "__main__":
    menu_main()

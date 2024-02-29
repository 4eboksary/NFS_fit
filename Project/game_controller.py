import pygame
import pygame.freetype
from my_car import MyCar
from globals import Globals


class GameController:

    def game_start(screen):
        """starts the game
        """
        clock = pygame.time.Clock()

        def game(screen):
            my_car = MyCar((400, 300), 270, Globals.CAR_CONTAINER[2], (50, 102))
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                keys_pressed = pygame.key.get_pressed()
                my_car.car_control(keys_pressed)

                screen.fill(Globals.BG_COLOR)
                my_car.draw(screen)
                pygame.display.flip()
                clock.tick(60)

        game(screen)

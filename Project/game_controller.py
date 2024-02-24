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
            my_car_image = MyCar.get_car_image('images/car2.png', (50, 68))
            my_car = MyCar((400, 300), 270, my_car_image, 1, 130, 10)
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

    
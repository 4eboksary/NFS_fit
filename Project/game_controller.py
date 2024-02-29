import pygame
import pygame.freetype
from my_car import MyCar
from my_map import MyMap, Checkpoint
from globals import Globals


class GameController:


    def game_start(screen):
        """starts the game
        """
        clock = pygame.time.Clock()
        def game(screen):
            my_car_image = MyCar.get_car_image('images/car2.png', (50, 68))
            my_car = MyCar((400, 300), 270, my_car_image, 1, 130, 10)
            my_map = MyMap('images/road.png', Globals.WIDTH, Globals.HEIGHT, 0, 0)
            #приклад створення чекпоінтів
            checkpoint1 = Checkpoint(screen, 100, 100)
            checkpoint2 = Checkpoint(screen, 400, 300)
            checkpoint3 = Checkpoint(screen, 700, 500)
            my_map.add_checkpoint(checkpoint1)
            my_map.add_checkpoint(checkpoint2)
            my_map.add_checkpoint(checkpoint3)
            running = True
            while running:
                for event in pygame.event.get():
                    my_map.draw()
                    if event.type == pygame.QUIT:
                        running = False

                keys_pressed = pygame.key.get_pressed()
                my_car.car_control(keys_pressed)

                screen.fill(Globals.BG_COLOR)
                my_car.draw(screen)
                pygame.display.flip()
                clock.tick(60) 
        
        game(screen)

    
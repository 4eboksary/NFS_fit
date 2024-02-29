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
            my_car_image = Globals.get_image('images/car2.png', (50, 68))
            my_car = MyCar((400, 300), 270, my_car_image, 1, 130, 10)
            my_map_image = Globals.get_image('images/road.png', (1200, 800))
            my_map_image = pygame.transform.rotate(my_map_image, 180)
            my_map = MyMap(my_map_image, 1200, 800, 0, 0)

            # Приклад створення чекпоінтів
            checkpoint1 = Checkpoint(my_map_image, 100, 100)
            checkpoint2 = Checkpoint(my_map_image, 400, 300)
            checkpoint3 = Checkpoint(my_map_image, 700, 500)

            # Додаємо чекпойнти до my_map
            '''my_map.add_checkpoint(checkpoint1)
            my_map.add_checkpoint(checkpoint2)
            my_map.add_checkpoint(checkpoint3)'''
            running = True
            while running:
                for event in pygame.event.get():
                    my_map.draw(screen)
                    if event.type == pygame.QUIT:
                        running = False

                keys_pressed = pygame.key.get_pressed()
                my_car.car_control(keys_pressed)

                screen.fill(Globals.BG_COLOR)
                my_map.draw(screen)
                my_car.draw(screen)
                pygame.display.flip()

                clock.tick(60)
        
        game(screen)

    
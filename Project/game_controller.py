import pygame
import pygame.freetype
from my_car import MyCar
from my_map import MyMap
from globals import Globals
from os.path import join


class GameController:
    @staticmethod
    def game_start(screen, car):
        """starts the game
        """
        clock = pygame.time.Clock()

        def show_win_message(screen) :
            win_font = pygame.font.Font(None, 70)
            text_surf = win_font.render("Win", True, (0, 255, 255))
            text_rect = text_surf.get_rect(center=(Globals.WIDTH / 2, Globals.HEIGHT / 2))
            screen.blit(text_surf, text_rect)

        def game(screen):
            my_car = MyCar((400, 300), 270, car)
            my_map_image = pygame.image.load(join('images', 'maps', 'road.png'))
            image_map = pygame.transform.scale(my_map_image, (Globals.WIDTH, Globals.HEIGHT)) 
            my_map = MyMap(image_map, Globals.WIDTH, Globals.HEIGHT, 0, 0)
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                keys_pressed = pygame.key.get_pressed()
                my_car.car_control(keys_pressed)     
                screen.fill(Globals.BG_COLOR)
                my_map.draw(screen)
                my_car.draw(screen)

                if my_map.check_win(my_car) :
                    show_win_message(screen)

                pygame.display.flip()
                clock.tick(60)
                
                

                    

        game(screen)


    
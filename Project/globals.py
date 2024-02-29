import pygame

class Globals:
    '''коефіцієнт для кординат

    start = (0.891;0.739)
    chkp1 = (0.891;0.302)
    chkp2 = (0.48;0.078)
    chkp3 = (0.062;0.474)
    chkp4 = (0.891;0.732)'''
    WIDTH = 1200
    HEIGHT = 800
    BG_COLOR = (50, 50, 50)
    def get_image(filename, size):
        image = pygame.image.load(filename)
        image = pygame.transform.scale(image, size)
        return image

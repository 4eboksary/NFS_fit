import pygame


def mock_get_car_image(image_name, size):
    image = pygame.image.load(image_name)
    image = pygame.transform.scale(image, size)
    return image

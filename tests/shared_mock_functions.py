from os.path import join

import pygame

from car_model import CarModel
from my_car import MyCar


def mock_get_car_image(image_name, size):
    image = pygame.image.load(image_name)
    image = pygame.transform.scale(image, size)
    return image


def my_car_mock(position=(0, 0), acceleration=1, max_speed=130, angle=90, mobility=5) -> MyCar:
    car = CarModel("Mock", join('images', 'cars', 'car1.png'), acceleration, max_speed, mobility, (5, 5))
    return MyCar(position, angle, car)

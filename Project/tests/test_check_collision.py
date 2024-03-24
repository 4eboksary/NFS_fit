from my_map import Checkpoint
from my_car import MyCar
from globals import Globals
from os.path import join
import pytest
import pygame


@pytest.mark.parametrize("car_coords, expected_result", [
    ((0, 0), True),
    ((300, 300), False)
])
def test_check_checkpoints(car_coords, expected_result, monkeypatch):


    def mock_get_car_image(image_name, size):
        image = pygame.image.load(image_name)
        image = pygame.transform.scale(image, size)
        return image
    
    
    monkeypatch.setattr("my_car.get_car_image", mock_get_car_image)
    my_map_image = pygame.image.load(join('images', 'maps', 'road.png'))
    image_map = pygame.transform.scale(my_map_image, (0, 0))
    checkpoint = Checkpoint(image_map, 0, 0)
    test_car = MyCar(car_coords, 270, Globals.CAR_CONTAINER[0])


    checkpoint.check_collision(test_car)
    assert checkpoint.is_crossed == expected_result

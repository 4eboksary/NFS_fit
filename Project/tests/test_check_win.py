from my_map import MyMap
from os.path import join
import pygame
import pytest


def mock_check_checpoints(my_map, check_is_crossed):
        for checkpoint in my_map.checkpoints:
            checkpoint.is_crossed = check_is_crossed

@pytest.mark.parametrize('mock_funk, check_is_crossed, expected_result', [
    (mock_check_checpoints, True, True),
    (mock_check_checpoints, False, False)
])
def test_check_win_true(mock_funk, check_is_crossed ,expected_result, monkeypatch):
     
     my_map_image = pygame.image.load(join('images', 'maps', 'road.png'))
     image_map = pygame.transform.scale(my_map_image, (0, 0)) 
     my_map = MyMap(image_map, 0, 0, 0, 0)
   
     monkeypatch.setattr("my_map.MyMap.check_checkpoints", mock_funk)

     assert my_map.check_win(check_is_crossed) == expected_result





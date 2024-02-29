from car_container import CarContainer
from player import Player


class Globals:
    WIDTH = 1200
    HEIGHT = 800
    BG_COLOR = (50, 50, 50)
    SAVE = Player("Illya", '0', available_cars={0, 1})
    CAR_CONTAINER = CarContainer().car_container

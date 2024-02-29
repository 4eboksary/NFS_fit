from car_container import CarContainer
import argparse


class Globals:
    WIDTH = 1200
    HEIGHT = 800
    BG_COLOR = (50, 50, 50)
    CAR_CONTAINER = CarContainer().car_container
    parser = argparse.ArgumentParser(description='show vectors')
    parser.add_argument('--show_vec', metavar='show_vec', type=str, help='enter true or false')
    args = parser.parse_args()




import json

from os.path import join

import pygame

from car_model import CarModel


class CarContainer:
    def __init__(self):
        json_path = join('json_files', 'cars.json')
        with open(json_path, 'r') as openfile:
            json_object = json.load(openfile)

        self.car_container = []
        for car in json_object:
            model_path = join('images', car['image'])
            self.car_container.append(CarModel(car['name'],
                                               model_path,
                                               car['acceleration'],
                                               car['max_speed'],
                                               car['mobility'],
                                               (car['size'][0], car['size'][1])))
import json
import os
from car import Car


class CarContainer:
    def __init__(self):
        json_path = os.path.join('json_files', 'cars.json')
        with open(json_path, 'r') as openfile:
            json_object = json.load(openfile)

        self.car_container = []
        for car in json_object:
            model_path = os.path.join('images', car['image'])
            self.car_container.append(Car(car['name'],
                                          model_path,
                                          car['acceleration'],
                                          car['max_speed'],
                                          car['mobility']))

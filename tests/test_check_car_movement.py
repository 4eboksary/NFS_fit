import pytest

from globals import Globals
from my_car import MyCar
from tests import shared_mock_functions


@pytest.mark.parametrize("position, speed, expected_movement",
                         [((0, 0), 60, True),
                          ((-70, 50), -60, False)])
def test_check_car_movement(position, speed, expected_movement, monkeypatch):
    def my_car_mock():
        angle = 90
        car = Globals.CAR_CONTAINER[0]
        return MyCar(position, angle, car)

    monkeypatch.setattr("my_car.get_car_image", shared_mock_functions.mock_get_car_image)

    test_subject = my_car_mock()
    test_subject.speed = speed
    car_position = position
    test_subject.move()

    assert (test_subject.rect.center[1] - car_position[1] > 0) == expected_movement

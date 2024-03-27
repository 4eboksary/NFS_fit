import pytest

from tests import shared_mock_functions


@pytest.mark.parametrize("position, speed, direction, expected_movement",
                         [((0, 0), 60, 1, True),
                          ((-70, 50), 60, -1, False)])
def test_check_car_movement(position, speed, direction, expected_movement, monkeypatch):
    monkeypatch.setattr("my_car.get_car_image", shared_mock_functions.mock_get_car_image)
    test_subject = shared_mock_functions.my_car_mock(position, 5)
    test_subject.speed = speed * direction
    car_position = position
    test_subject.move()

    assert (test_subject.rect.center[1] - car_position[1] > 0) == expected_movement

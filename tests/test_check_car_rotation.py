import pytest
from tests import shared_mock_functions


@pytest.mark.parametrize("position, speed, direction, expected_movement",
                         [((0, 0), 60, 1, True),
                          ((-70, 50), 60, -1, False)])
def test_check_car_rotation(position, speed, direction, expected_movement, monkeypatch):
    monkeypatch.setattr("my_car.get_car_image", shared_mock_functions.mock_get_car_image)
    test_subject = shared_mock_functions.my_car_mock(position, 5)
    test_subject.speed = speed * direction
    test_subject.move()
    initial_angle = test_subject.angle
    y_rotation = 10
    test_subject.rotate(y_rotation)

    assert test_subject.angle == initial_angle - ( -y_rotation * test_subject.mobility * test_subject.speed_func[test_subject.speed]) % 360
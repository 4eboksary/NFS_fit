import pytest

from tests import shared_mock_functions


@pytest.mark.parametrize("acceleration, max_speed, mobility, expected", [(1, 2, 1, [0, -0.75, -1])])
def test_check_speed_curve_creation(acceleration, max_speed, mobility, expected, monkeypatch):
    monkeypatch.setattr("my_car.get_car_image", shared_mock_functions.mock_get_car_image)
    test_subject = shared_mock_functions.my_car_mock(acceleration=acceleration, max_speed=max_speed, mobility=mobility)
    curve = test_subject.speed_curve_creation()
    for i in range(0, len(curve)):
        assert curve[i] == expected[i]

import pytest

from menu_controller import chooser_wheel


@pytest.mark.car
@pytest.mark.parametrize('index, step, length, ticks, expected_index, test_result',
                         [(2, 5, 32, 1, 7, True),
                          (2, -5, 32, 1, -3, False)])
def test_check_choose_wheel(index, step, length, ticks, expected_index, test_result, monkeypatch):
    i = 0
    for _ in range(0, ticks):
        i = chooser_wheel(index, step, length)
    assert (expected_index == i) == test_result

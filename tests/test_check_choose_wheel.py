import pytest

from menu_controller import chooser_wheel


@pytest.mark.parametrize('index, step, length, ticks, expected_index, test_result',
                         [(2, 5, 32, 1, 7, True),
                          (2, -5, 32, 1, -3, False)])
def test_check_choose_wheel(index, step, length, ticks, expected_index, test_result, monkeypatch):
    monkeypatch.setattr('pygame.init', lambda *args: None)
    monkeypatch.setattr('pygame.display.set_mode', lambda *args: None)
    monkeypatch.setattr('pygame.display.set_caption', lambda *args: None)
    i = 0
    for _ in range(0, ticks):
        i = chooser_wheel(index, step, length)
    assert (expected_index == i) == test_result

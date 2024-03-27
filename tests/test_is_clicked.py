import pytest
from os.path import join
from button import ButtonImage
from globals import Globals

@pytest.fixture()
def button():
    # Ініціалізуємо об'єкт класу для тестування
    return ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 2, 300, 130, join('images', 'buttons', 'button_play.png'))

def test_is_clicked_returns_true_when_point_inside_rect(button):
    # Тестуємо, чи повертає метод is_clicked значення True,
    # коли передана позиція знаходиться всередині прямокутника кнопки
    pos_inside = (Globals.WIDTH / 2 + 50, Globals.HEIGHT / 2 + 50)  # Позиція всередині кнопки
    assert button.is_clicked(pos_inside) is True

def test_is_clicked_returns_false_when_point_outside_rect(button):
    # Тестуємо, чи повертає метод is_clicked значення False,
    # коли передана позиція знаходиться поза прямокутником кнопки
    pos_outside = (Globals.WIDTH / 2 + 100, Globals.HEIGHT / 2 + 100)  # Позиція поза кнопкою
    assert button.is_clicked(pos_outside) is False
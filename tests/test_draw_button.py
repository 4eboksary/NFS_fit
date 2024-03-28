import pytest
import pygame
from os.path import join
from globals import Globals
from button import ButtonImage

@pytest.fixture()
def button():
    # Ініціалізуємо об'єкт класу для тестування
    return ButtonImage(Globals.WIDTH / 2, Globals.HEIGHT / 2, 300, 130, join('images', 'buttons', 'button_play.png'))

 #Параметри для першого тесту
@pytest.mark.parametrize("width, height, center", [
    (300, 130, (600, 400)),
    (100, 100, (525, 533)),
    (95, 95, (675, 533)),
])
def test_draw_button(button, width, height, center):
    # Створюємо екран для тестування
    screen = pygame.Surface((1200, 800))

    # Встановлюємо нові розміри та позицію кнопки
    button.rect.width = width
    button.rect.height = height
    button.rect.center = center

    button.draw(screen)

    # Перевіряємо, чи зображення кнопки коректно відображається на екрані
    assert button.rect.width == width
    assert button.rect.height == height
    assert button.rect.center == center
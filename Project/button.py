import pygame
class ButtonImage:
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path) #завантажуємо фото

        self.image = pygame.transform.scale(self.image, (width, height)) #підганяємо під наш розмір

        self.rect = self.image.get_rect(topleft=(x, y))

        self.is_hovered = False

        #малюємо основу для кнопок:
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    #обробка натискання кнопки
    def handle_click(self):
        if self.is_hovered:
            print("")
           #Тут будуть виконатися додаткові дії, які повинні відбутися при натисканні кнопки.
            #Наприклад, відкриття нового вікна тощо.


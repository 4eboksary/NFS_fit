import pygame
class ButtonImage:
    def _init_(self, x, y, width, height, text, imagepath):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = pygame.image.load(imagepath) #завантажуємо фото

        self.image = pygame.transform.scale(self.image, (width, height)) #підганяємо під наш розмір

        self.rect = self.image.get_rect(topleft=(x, y))

        self.is_hovered = False

        #малюємо основу для кнопок:
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    #перевірка чи наведена мишка на кнопку
    def check_hover(self, pos_mouse):
        self.is_hovered = self.rect.collidepoint(pos_mouse)

    #обробка натискання кнопки
    def handle_click(self):
        if self.is_hovered:
            print(f"Button '{self.text}' was clicked!")
           #Тут будуть виконатися додаткові дії, які повинні відбутися при натисканні кнопки.
            #Наприклад, відкриття нового вікна тощо.


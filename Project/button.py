import pygame
class button_image:
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path) #завантажуємо фото
        self.image = pygame.transform.scale(self.image, (width, height)) #підганяємо під наш розмір
        self.rect = self.image.get_rect(topleft=(x, y))

        #малюємо основу для кнопок:
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)



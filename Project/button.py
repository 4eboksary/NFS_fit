import pygame
class ButtonImage:
    def __init__(self, x, y, width, height, image_path):
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path) #завантажуємо фото
        self.image = pygame.transform.scale(self.image, (width, height)) #підганяємо під наш розмір
        self.rect = self.image.get_rect(center=(x, y))

        #малюємо основу для кнопок:
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def set_pos(self, x, y):
        self.rect = self.image.get_rect(center=(x, y))



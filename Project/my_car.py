class MyCar:
    def __init__(self,position, image):
        self.image = image
        self.rect = self.image.get_rect
        self.rect.center = position
    def draw(self, screen):
        screen.blit(self.image, self.rect)
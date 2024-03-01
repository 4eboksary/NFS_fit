import pygame
from os.path import join


class MyMap:
    def __init__(self, surface, width, height, pos_x, pos_y):
        self.surface = surface
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(join('images','maps','road.png'))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)
        self.max_speed = 10
        self.checkpoints = []
        checkpoint1 = Checkpoint(self.surface, 100, 250)
        checkpoint2 = Checkpoint(self.surface, 450, 30)
        checkpoint3 = Checkpoint(self.surface, 850, 250)
        checkpoint4 = Checkpoint(self.surface, 450, 500)
        self.add_checkpoint(checkpoint1)
        self.add_checkpoint(checkpoint2)
        self.add_checkpoint(checkpoint3)
        self.add_checkpoint(checkpoint4)
        self.draw(self.surface)


    def draw(self, screen):
        screen.blit(self.surface, (self.pos_x, self.pos_y))
        for checkpoint in self.checkpoints: # Якщо чекпоінт не перетнутий
            checkpoint.draw()

    '''def check_collision(self, car):
        if car.rect.colliderect(self.rect):
            # Зменшити максимальну швидкість машини
            car.max_speed = 5
        else:
            # Відновити максимальну швидкість машини
            car.max_speed = 10'''

    def add_checkpoint(self, checkpoint):
        self.checkpoints.append(checkpoint)


    def check_win(self, car):
        # Перевірити, чи перетнув гравець всі чекпоінти
        self.check_checkpoints(car)
        is_win = True
        for checkpoint in self.checkpoints:
            if not checkpoint.is_crossed:
                is_win = False
        return is_win
    

    def check_checkpoints(self, car) :
        for checkpoint in self.checkpoints:
            checkpoint.check_collision(car)

class Checkpoint:
    def __init__(self, surface, pos_x, pos_y):
        self.surface = surface
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(join('images','maps','checkpoint.png'))
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.pos_x, self.pos_y)
        self.is_crossed = False

    def draw(self):
        self.surface.blit(self.image, self.rect)

    def check_collision(self, car):
        if car.rect.colliderect(self.rect) and not self.is_crossed :
            self.is_crossed = True

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
        self.checkpoints = [
            Checkpoint(self.surface, 100, 100),
            Checkpoint(self.surface, 200, 200),
            Checkpoint(self.surface, 300, 300),
            Checkpoint(self.surface, 400, 400)]

    def draw(self, screen):
        screen.blit(self.surface, (self.pos_x, self.pos_y))
        for checkpoint in self.checkpoints:
            if not checkpoint.is_crossed:  # Якщо чекпоінт не перетнутий
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

    def check_win(self):
        # Перевірити, чи перетнув гравець всі чекпоінти
        for checkpoint in self.checkpoints:
            if not checkpoint.is_crossed:
                return False

        '''# Перевірити, чи вклався гравець у часовий ліміт
        if time.time() - self.start_time > time_limit:
            return False'''

        return True

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
        if car.rect.colliderect(self.rect) and not self.is_crossed:
            self.is_crossed = True

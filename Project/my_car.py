import math

import pygame


class MyCar:
    def __init__(self, position, angle,  image, acceleration, max_speed):
        self.image = image
        self.new_image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.max_speed = max_speed
        self.speed = 0
        self.angle = angle
        self.acceleration = acceleration
        self.vector = pygame.Vector2(0, -self.image.get_width() / 2)
        self.r = math.sqrt(
            (position[0] - (position[0] + self.vector.x)) ** 2 + (position[1] - (position[1] + self.vector.y)) ** 2)

    def move(self):
        self.vector.x = self.r * math.cos(self.angle * math.pi / 180)
        self.vector.y = self.r * math.sin(self.angle * math.pi / 180)
        self.rect.x += self.vector.x * 0.1 * self.speed
        self.rect.y += self.vector.y * 0.1 * self.speed

    def rotate(self, y):
        self.angle -= y
        self.new_image = pygame.transform.rotate(self.image, - self.angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)
        if self.angle >= 360:
            self.angle -= 360
        if self.angle < 0:
            self.angle += 360

    def draw(self, screen):
        screen.blit(self.new_image, self.rect)
        print(self.vector, self.rect.center, self.angle)
        pygame.draw.circle(screen, color="red", center=self.rect.center + self.vector, radius=5)

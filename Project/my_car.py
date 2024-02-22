import math
import numpy
import pygame


class MyCar:
    def __init__(self, position, angle, image, acceleration, max_speed, mobility):
        self.image = image
        self.max_speed = max_speed
        self.speed = 0
        self.mobility = mobility
        self.angle = angle
        self.rotated_image = pygame.transform.rotate(self.image, - self.angle - 90)
        self.rect = self.rotated_image.get_rect()
        self.rect.center = position
        self.acceleration = acceleration
        self.vector = pygame.Vector2(0, -self.image.get_width() / 2)
        self.r = math.sqrt(
            (position[0] - (position[0] + self.vector.x)) ** 2 + (position[1] - (position[1] + self.vector.y)) ** 2)
        self.speed_func = MyCar.speed_curve_creation(self)

    def move(self):
        self.vector.x = self.r * math.cos(self.angle * math.pi / 180)
        self.vector.y = self.r * math.sin(self.angle * math.pi / 180)
        self.rect.x += self.vector.x * 0.0035 * self.speed
        self.rect.y += self.vector.y * 0.0035 * self.speed
        self.speed = round(self.speed, 5)

    def rotate(self, y):
        self.angle -= -y * self.mobility * self.speed_func[self.speed]
        self.rotated_image = pygame.transform.rotate(self.image, - self.angle - 90)
        self.rect = self.rotated_image.get_rect(center=self.rect.center)
        self.angle %= 360

    def draw(self, screen):
        screen.blit(self.rotated_image, self.rect)
        print(self.vector, self.rect.center, self.angle, self.speed)
        # pygame.draw.circle(screen, color="red", center=self.rect.center + self.vector, radius=5)
        # pygame.draw.circle(screen, color="blue", center=self.rect.center, radius=5)

    def speed_curve_creation(self):
        lin = numpy.linspace(0, self.max_speed - 5, self.max_speed + 1)
        zero_y = 1 / ((self.max_speed * self.max_speed) / (-4))
        return zero_y * (- lin * lin + self.max_speed * lin)

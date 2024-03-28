import math

import numpy
import pygame


def get_car_image(image_name, size):
    image = pygame.image.load(image_name).convert_alpha()
    image = pygame.transform.scale(image, size)
    return image


class MyCar:
    def __init__(self, position, angle, car):
        self.image = get_car_image(car.image, car.size)
        self.max_speed = car.max_speed
        self.speed = 0
        self.mobility = car.mobility
        self.angle = angle
        self.rotated_image = pygame.transform.rotate(self.image, - self.angle - 90)
        self.rect = self.rotated_image.get_rect()
        self.rect.center = position
        self.acceleration = car.acceleration
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
        # if Globals.args.dev == "True":
        #     print(self.vector, self.rect.center, self.angle, self.speed)
        # if Globals.args.show_vec == "True":
        #     pygame.draw.circle(screen, color="red", center=self.rect.center + self.vector, radius=5)
        #     pygame.draw.circle(screen, color="blue", center=self.rect.center, radius=5)

    def speed_curve_creation(self):
        lin = numpy.linspace(0, self.max_speed - self.mobility, self.max_speed + self.acceleration)
        zero_y = 1 / ((self.max_speed * self.max_speed) / (-4))
        return zero_y * (- lin * lin + self.max_speed * lin)

    def car_control(self, keys):
        speed_decay = 1
        if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_w] or keys[pygame.K_s]:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                if self.speed < self.max_speed:
                    self.speed += self.acceleration
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                if self.speed > - self.max_speed * 0.5:
                    self.speed -= self.acceleration * 2
        else:
            if self.speed > 0:
                self.speed -= speed_decay
            elif self.speed < 0:
                self.speed += speed_decay

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(0.5)
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(-0.5)
        self.move()

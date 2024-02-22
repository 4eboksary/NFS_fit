import pygame
import pygame.freetype
from my_car import MyCar
from globals import Globals

pygame.init()

clock = pygame.time.Clock()

global_vars = Globals()
screen = pygame.display.set_mode((global_vars.screen_width, global_vars.screen_height))

pygame.display.set_caption("екн ерші")
background_color = global_vars.bg_color


def get_car_image(filename, size):
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.scale(image, size)
    return image


def car_control(keys):
    speed_decay = 1
    if keys[pygame.K_UP] or keys[pygame.K_DOWN] or keys[pygame.K_w] or keys[pygame.K_s]:
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            if my_car.speed < my_car.max_speed:
                my_car.speed += my_car.acceleration
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            if my_car.speed > - my_car.max_speed * 0.5:
                my_car.speed -= my_car.acceleration * 2
    else:
        if my_car.speed > 0:
            my_car.speed -= speed_decay
        elif my_car.speed < 0:
            my_car.speed += speed_decay

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        my_car.rotate(0.5)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        my_car.rotate(-0.5)
    my_car.move()


my_car_image = get_car_image('images/car2.png', (50, 68))
my_car = MyCar((400, 300), 270, my_car_image, 1, 130, 10)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    car_control(keys_pressed)

    screen.fill(background_color)
    my_car.draw(screen)
    pygame.display.flip()
    clock.tick(60)

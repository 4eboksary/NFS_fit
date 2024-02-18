import pygame
import pygame.freetype
from my_car import MyCar

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("екн ерші")
background_color = (50, 50, 30)


def get_car_image(filename, size, angle):
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image


my_car_image = get_car_image('Project/images/car2.png', (50, 68), 0)

my_car = MyCar((400, 300), 270, my_car_image, 0.05, 2)
running = True
angle = 0
pos = [400, 300]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     if my_car.speed <= my_car.max_speed:
    #         my_car.speed += my_car.acceleration
    #     my_car.move(-my_car.speed, 0)
    # if keys[pygame.K_RIGHT]:
    #     my_car.move(my_car.speed, 0)
    # if keys[pygame.K_UP]:
    #     if my_car.speed <= my_car.max_speed:
    #         my_car.speed += my_car.acceleration
    #     my_car.move(0, -my_car.speed)
    # if keys[pygame.K_DOWN]:
    #     if my_car.speed <= my_car.max_speed:
    #         my_car.speed += my_car.acceleration
    #     my_car.move(0, my_car.speed)

    if keys[pygame.K_UP]:
        if my_car.speed <= my_car.max_speed:
            my_car.speed += my_car.acceleration
        my_car.move()
        if keys[pygame.K_LEFT]:
            my_car.rotate(5)
        if keys[pygame.K_RIGHT]:
            my_car.rotate(-5)
    else:
        if my_car.speed > 0:
            my_car.speed -= my_car.acceleration
            my_car.move()


    screen.fill(background_color)
    my_car.draw(screen)
    pygame.display.flip()
    clock.tick(60)

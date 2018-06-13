# Brendon Nguyen, Jack Sparkman
# June 11, 2018
import pygame
import view
import settings

screen = settings.init.screen
clock = settings.init.clock
x = settings.x
y = settings.y
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        y -= 3
    if pressed[pygame.K_s]:
        y += 3
    if pressed[pygame.K_a]:
        x -= 3
    if pressed[pygame.K_d]:
        x += 3
    if pressed[pygame.K_UP]:
        continue
    view
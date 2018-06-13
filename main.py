# Brendon Nguyen, Jack Sparkman
# June 11, 2018

import pygame, controller

pygame.init()
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        controller

        pygame.display.flip()

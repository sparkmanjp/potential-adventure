# Brendon Nguyen, Jack Sparkman
# June 11, 2018

import pygame
import controller
import settings

pygame.init()
done = False

def main(done):
    while not done:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True
            controller.update_face()

            pygame.display.flip()

if __name__ == "__main__":
    main(False)

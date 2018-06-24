# Brendon Nguyen, Jack Sparkman
# June 11, 2018
import pygame
import settings

clock = settings.clock
screen = settings.screen
x = settings.FACE_X
y = settings.FACE_Y


screen.fill((0, 0, 0))
BLUE = (0, 128, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
color_circ = (255, 220, 210)

def draw_face():
    pygame.draw.circle(screen, color_circ, [x + 40, y + 40], 40)
    pygame.draw.circle(screen, BLUE, [x + 60, y + 40], 10)
    pygame.draw.circle(screen, BLUE, [x + 20, y + 40], 10)
    pygame.draw.circle(screen, BLACK, [x + 60, y + 40], 4)
    pygame.draw.circle(screen, BLACK, [x + 20, y + 40], 4)
    pygame.draw.ellipse(screen, RED, [x + 28, y + 50, 25, 15], 4)
    pygame.draw.ellipse(screen, color_circ, [x + 28, y + 54, 25, 15])
    pygame.display.flip()
    clock.tick(60)

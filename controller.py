# Brendon Nguyen, Jack Sparkman
# June 11, 2018
import pygame
import view
import settings

pygame.init()
screen = pygame.display.set_mode((800, 600))
game_over = False
is_blue = True
x = 30
y = 30

# def update_face(x, y, done):
#     done = False
#     while not done:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
#
# while not game_over:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#             is_blue = not is_blue
#
#     pressed = pygame.key.get_pressed()
#     if pressed[pygame.K_w]: y -= 3
#     if pressed[pygame.K_s]: y += 3
#     if pressed[pygame.K_a]: x -= 3
#     if pressed[pygame.K_d]: x += 3
#     if pressed[pygame.K_UP]:
#         continue
#
#     screen.fill((0, 0, 0))
#     BLUE = (0, 128, 255)
#     BLACK = (0, 0, 0)
#     RED = (255, 0, 0)
#     color_circ = (255,220,210)
#     pygame.draw.circle(screen, color_circ, [x + 40, y + 40], 40)
#     pygame.draw.circle(screen, BLUE, [x + 60, y + 40], 10)
#     pygame.draw.circle(screen, BLUE, [x + 20, y + 40], 10)
#     pygame.draw.circle(screen, BLACK, [x + 60, y + 40], 4)
#     pygame.draw.circle(screen, BLACK, [x + 20, y + 40], 4)
#     pygame.draw.ellipse(screen, RED, [x + 28, y + 50, 25, 15], 4)
#     pygame.draw.ellipse(screen, color_circ, [x + 28, y + 54, 25, 15])
#     pygame.display.flip()
#     clock.tick(60)

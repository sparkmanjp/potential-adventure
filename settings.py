import pygame


def init():
    import controller
    import view
    import main

    def screen():
        global screen
        screen = pygame.display.set_mode((800, 600))

    def x():
        global x
        x = 30

    def y():
        global y
        y = 30

    def clock():
        global clock
        clock = pygame.time.Clock()


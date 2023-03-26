import pygame
import time
import constants
import game

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame_icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(pygame_icon)

w, h = screen.get_size()

running = True

GAME = game.Game(pygame, screen)


last = time.time_ns()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    now = time.time_ns()
    deltaTime = now - last
    last = now

    screen.fill((255, 255, 255))

    GAME.update(deltaTime)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

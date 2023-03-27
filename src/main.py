import time

import pygame

import game
import screens

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame_icon = pygame.image.load('assets/icon.png')
pygame.display.set_icon(pygame_icon)

w, h = screen.get_size()

game.pygame = pygame
game.screen = screen
game.currentscreen = screens.MainMenu()
game.currentscreen.init()


last = time.time_ns()


while game.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.stop()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            game.click(mx, my)
    now = time.time_ns()
    deltaTime = now - last
    last = now

    screen.fill((255, 255, 255))

    game.update(deltaTime)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

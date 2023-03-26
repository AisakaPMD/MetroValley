import pygame
import time

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame_icon = pygame.image.load('../assets/icon.png')
pygame.display.set_icon(pygame_icon)

w, h = screen.get_size()

running = True

SCREEN_MAIN_MENU = "main_menu"
SCREEN_LOADING = "loading"
SCREEN_GAME = "game"

currentScreen = SCREEN_MAIN_MENU

last = time.time_ns()

splash = pygame.image.load('../assets/splash.png')

def updateMainMenu(delta):
    screen.blit(splash, (w / 2 - splash.get_width() / 2, 30))


def updateLoading(delta):
    pass


def updateGame(deltaTime):
    pass


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    now = time.time_ns()
    deltaTime = now - last
    last = now

    screen.fill((255, 255, 255))
    if currentScreen == SCREEN_MAIN_MENU:
        updateMainMenu(deltaTime)
    elif currentScreen == SCREEN_LOADING:
        updateLoading(deltaTime)
    elif currentScreen == SCREEN_GAME:
        updateGame(deltaTime)

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

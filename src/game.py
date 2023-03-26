import constants
import screens

class Game:
    def __init__(self, pygame, screen):
        self.screen = screen
        self.pygame = pygame
        self.currentScreen = screens.MainMenu(pygame, screen)
        self.currentScreen.init()

    def update(self, delta):
        self.currentScreen.update(delta=delta)


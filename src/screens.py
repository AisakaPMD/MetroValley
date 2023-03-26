from abc import ABC, abstractmethod
import tiling


class Screen(ABC):
    def __int__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen

    @abstractmethod
    def update(self, delta):
        pass

    @abstractmethod
    def init(self):
        pass

    @abstractmethod
    def deinit(self):
        pass

    @abstractmethod
    def onclick(self, x, y):
        pass


class MainMenu(Screen):
    def __init__(self, pygame, screen):
        self.splash = None
        self.buttonmap = None
        self.pygame = pygame
        self.screen = screen

    def update(self, delta):
        self.screen.blit(self.splash, (self.screen.get_size()[0] / 2 - self.splash.get_width() / 2, 30))
        self.screen.blit(self.buttonmap, (self.screen.get_size()[0] / 2 - self.splash.get_width() / 2, 30))

    def init(self):
        self.splash = self.pygame.image.load('assets/splash.png')
        self.buttonmap = tiling.Tilemap(self.pygame, 'assets/textures/TitleButtons.png')
        self.buttonmap.addTile("new_idle", (0, 187, 74, 58))
        self.buttonmap.addTile("new_hover", (0, 245, 74, 58))

        self.buttonmap.addTile("load_idle", (74, 187, 74, 58))
        self.buttonmap.addTile("load_hover", (74, 245, 74, 58))

        self.buttonmap.addTile("exit_idle", (222, 187, 74, 58))
        self.buttonmap.addTile("exit_hover", (222, 245, 74, 58))

    def deinit(self):
        del self.splash

    def onclick(self, x, y):
        pass

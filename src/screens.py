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
        self.buttonSpacing = 20
        self.buttonWidth = 74
        self.buttonHeight = 58

    def update(self, delta):
        self.screen.blit(self.splash, (self.screen.get_size()[0] / 2 - self.splash.get_width() / 2, 30))
        new = (self.screen.get_size()[0] / 2 - self.buttonWidth*1.5 - self.buttonSpacing, 30*2+ 500)
        load = (self.screen.get_size()[0] / 2 - self.buttonWidth*0.5, 30*2+ 500)
        exit = (self.screen.get_size()[0] / 2 + self.buttonWidth*0.5 + self.buttonSpacing, 30*2+ 500)
        mx, my = self.pygame.mouse.get_pos()
        newh = mx > new[0] and mx < (new[0] + self.buttonWidth) and my > new[1] and my < (new[1] + self.buttonHeight)
        loadh = mx > load[0] and mx < (load[0] + self.buttonWidth) and my > load[1] and my < (load[1] + self.buttonHeight)
        exith = mx > exit[0] and mx < (exit[0] + self.buttonWidth) and my > exit[1] and my < (exit[1] + self.buttonHeight)
        self.screen.blit(self.buttonmap.get("new_idle" if not newh else "new_hover"), new)
        self.screen.blit(self.buttonmap.get("load_idle" if not loadh else "load_hover"), load)
        self.screen.blit(self.buttonmap.get("exit_idle" if not exith else "exit_hover"), exit)


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

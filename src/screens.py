from abc import ABC, abstractmethod
import tiling
import game


class Screen(ABC):
    def __int__(self):
        pass

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
    def __init__(self):
        self.splash = None
        self.buttonmap = None
        self.buttonSpacing = 20
        self.buttonWidth = 74
        self.buttonHeight = 58

    def get_buttons_position(self):
        return ((game.screen.get_size()[0] / 2 - self.buttonWidth*1.5 - self.buttonSpacing, 30 * 2 + 500),
                (game.screen.get_size()[0] / 2 - self.buttonWidth*0.5, 30 * 2 + 500),
                (game.screen.get_size()[0] / 2 + self.buttonWidth*0.5 + self.buttonSpacing, 30 * 2 + 500))

    def update(self, delta):
        game.screen.blit(self.splash, (game.screen.get_size()[0] / 2 - self.splash.get_width() / 2, 30))
        new, load, exitb = self.get_buttons_position()
        mx, my = game.pygame.mouse.get_pos()
        newh = new[0] < mx < (new[0] + self.buttonWidth) and new[1] < my < (new[1] + self.buttonHeight)
        loadh = load[0] < mx < (load[0] + self.buttonWidth) and load[1] < my < (load[1] + self.buttonHeight)
        exith = exitb[0] < mx < (exitb[0] + self.buttonWidth) and exitb[1] < my < (exitb[1] + self.buttonHeight)
        game.screen.blit(self.buttonmap.get("new_idle" if not newh else "new_hover"), new)
        game.screen.blit(self.buttonmap.get("load_idle" if not loadh else "load_hover"), load)
        game.screen.blit(self.buttonmap.get("exit_idle" if not exith else "exit_hover"), exitb)


    def init(self):
        self.splash = game.pygame.image.load('assets/splash.png')
        self.buttonmap = tiling.Tilemap(game.pygame, 'assets/textures/TitleButtons.png')
        self.buttonmap.addTile("new_idle", (0, 187, 74, 58))
        self.buttonmap.addTile("new_hover", (0, 245, 74, 58))

        self.buttonmap.addTile("load_idle", (74, 187, 74, 58))
        self.buttonmap.addTile("load_hover", (74, 245, 74, 58))

        self.buttonmap.addTile("exit_idle", (222, 187, 74, 58))
        self.buttonmap.addTile("exit_hover", (222, 245, 74, 58))

    def deinit(self):
        del self.splash
        del self.buttonmap

    def onclick(self, x, y):
        mx, my = game.pygame.mouse.get_pos()
        new, load, exitb = self.get_buttons_position()
        newh = new[0] < x < (new[0] + self.buttonWidth) and new[1] < y < (new[1] + self.buttonHeight)
        loadh = load[0] < x < (load[0] + self.buttonWidth) and load[1] < y < (load[1] + self.buttonHeight)
        exith = exitb[0] < x < (exitb[0] + self.buttonWidth) and exitb[1] < y < (exitb[1] + self.buttonHeight)
        if exith:
            game.stop()
        if loadh:
            pass
        if newh:
            # game.Game.create()
            pass

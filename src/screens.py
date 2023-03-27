from abc import ABC, abstractmethod
import tiling
import game
import player
import constants


class Screen(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self, delta):
        pass

    @abstractmethod
    def deinit(self):
        pass

    @abstractmethod
    def onclick(self, x, y):
        pass


class MainMenu(Screen):
    def __init__(self):
        self.buttonSpacing = 20
        self.buttonWidth = 74
        self.buttonHeight = 58
        self.splash = game.pygame.image.load('assets/splash.png')
        self.buttonmap = tiling.Tilemap(game.pygame, 'assets/textures/TitleButtons.png')
        self.buttonmap.addTile("new_idle", (0, 187, 74, 58))
        self.buttonmap.addTile("new_hover", (0, 245, 74, 58))

        self.buttonmap.addTile("load_idle", (74, 187, 74, 58))
        self.buttonmap.addTile("load_hover", (74, 245, 74, 58))

        self.buttonmap.addTile("exit_idle", (222, 187, 74, 58))
        self.buttonmap.addTile("exit_hover", (222, 245, 74, 58))

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
            game.create()


class Loading(Screen):
    def __init__(self):
        self.splash = game.pygame.image.load('assets/splash.png')

    def update(self, delta):
        game.screen.blit(self.splash, (game.screen.get_size()[0] / 2 - self.splash.get_width() / 2, 30))

    def deinit(self):
        del self.splash

    def onclick(self, x, y):
        pass

class Game(Screen):
    def __init__(self):
        self.tilemap = tiling.Tilemap(game.pygame, 'assets/textures/Cursors.fr-FR.png')
        self.tilemap.addTile("id"+str(constants.tile_grass_1), (464, 1648, 16, 16))

    def update(self, delta):
        # translate
        sw, sh = game.screen.get_size()
        px, py = player.user["pos"]
        tx, ty = sw/2 - (px*constants.tile_size), sh/2 - (py*constants.tile_size)
        for y in range(player.farm_map_size[1]):
            for x in range(player.farm_map_size[0]):
                print("id"+str(player.farm_map[y][x]))
                game.screen.blit(self.tilemap.get("id"+str(player.farm_map[y][x])), (tx+x*constants.tile_size, ty+y*constants.tile_size))

    def deinit(self):
        pass

    def onclick(self, x, y):
        pass

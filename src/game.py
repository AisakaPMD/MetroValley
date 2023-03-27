import player
import screens

running = True
screen = None
pygame = None
currentscreen = None


def stop():
    global running
    running = False


def update(delta):
    currentscreen.update(delta=delta)


def click(x, y):
    currentscreen.onclick(x, y)


def create():
    global currentscreen
    # put loading screen
    old = currentscreen
    currentscreen = screens.Loading()
    old.deinit()
    # create a new game
    player.load_map()

    player.user = {}
    player.user["pos"] = (1, 1)

    # save it
    player.save()

    old = currentscreen
    gamescreen = screens.Game()
    currentscreen = gamescreen
    old.deinit()


def load_game(filename):
    pass # TODO load a game into memory from binary file

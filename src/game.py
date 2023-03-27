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
    pass  # TODO create game

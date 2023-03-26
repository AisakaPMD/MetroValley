class Tilemap:
    def __init__(self, pygame, path):
        self.pygame = pygame
        self.path = path
        self.image = pygame.image.load(path)
        self.tiles = {}

    def addTile(self, p_id, rect):
        self.tiles[p_id] = rect

    def get(self, p_id):
        tile = self.tiles[p_id]
        return self.image.subsurface((tile[0], tile[1], tile[2], tile[3]))

import struct
import constants

farm_map_size = (0, 0)
farm_map = None
entities = None
user = None

def load_map():
	global farm_map_size
	global farm_map
	global user
	global entities
	fname = "assets/maps/farm_map.bin"
	mapf = open(fname, "rb")
	mapWidth = struct.unpack(">I", mapf.read(4))[0]
	mapHeight = struct.unpack(">I", mapf.read(4))[0]
	farm_map = []
	for y in range(mapHeight):
		farm_map.append([])
		for x in range(mapHeight):
			farm_map[y].append(struct.unpack(">B", mapf.read(1))[0])
	farm_map_size = (mapWidth, mapHeight)


def save():
	pass

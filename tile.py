from tile_type import TileType


class Tile:
	"""
	Represents a world tile, such as a wall, floor, tree, door, etc.
	"""
	def __init__(
		self,
		type: TileType # The static template that this in-world tile represents.
	):
		self.explored = False
		self.type = type
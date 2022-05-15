from copy import deepcopy

from color import Color
from glyph import Glyph


class TileType:
	"""
	A template class for Tiles.
	Holds the static data shared among all instances of a certain type of Tile.
	"""
	def __init__(
		self,
		name: str = "<Tile",
		solid: bool = False, # True if an entity can move through this tile (floor, open door, etc.)
		transparent: bool = True, # True if light and FOV can pass through this tile (floor, window, etc.)
		light_glyph: Glyph = Glyph(),
		dim_glyph: Glyph = Glyph(),
		dark_glyph: Glyph = Glyph()
	):
		self.name = name
		self.solid = solid
		self.transparent = transparent
		self.light_glyph = deepcopy(light_glyph)
		self.dim_glyph = deepcopy(dim_glyph)
		self.dark_glyph = deepcopy(dark_glyph)
	

	# Constants (overridden below due to Python limitations).
	DOOR_CLOSED = None
	DOOR_OPEN = None
	FLOOR = None
	WALL = None


# All constant Tile types (which serve as a base/template for spawning tiles).

TileType.DOOR_CLOSED = TileType(
	name = "Door (Closed)",
	solid = True,
	transparent = False,
	light_glyph = Glyph('≡', Color.BROWN),
	dim_glyph = Glyph('≡', Color.BROWN),
	dark_glyph = Glyph('≡', Color.DARK_GREY)
)

TileType.DOOR_OPEN = TileType(
	name = "Door (Open)",
	solid = False,
	transparent = True,
	light_glyph = Glyph('+', Color.BROWN),
	dim_glyph = Glyph('+', Color.BROWN),
	dark_glyph = Glyph('+', Color.DARK_GREY)
)

TileType.FLOOR = TileType(
	name = "Floor",
	solid = False,
	transparent = True,
	light_glyph = Glyph('.', Color.LIGHT_GREY),
	dim_glyph = Glyph('.', Color.GREY),
	dark_glyph = Glyph(' ', Color.DARK_GREY)
)

TileType.WALL = TileType(
	name = "Wall",
	solid = True,
	transparent = False,
	light_glyph = Glyph('#', Color.LIGHT_GREY),
	dim_glyph = Glyph('#', Color.GREY),
	dark_glyph = Glyph('#', Color.DARK_GREY)
)

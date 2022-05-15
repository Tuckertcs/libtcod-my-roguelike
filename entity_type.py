from copy import deepcopy

from color import Color
from glyph import Glyph


class EntityType:
	"""
	A template class for Entities.
	Holds the static data shared among all instances of a certain type of Entity.
	"""
	def __init__(
		self,
		name: str = "<Entity>",
		solid: bool = False, # True if an entity can move through this tile (floor, open door, etc.)
		glyph: Glyph = Glyph()
	):
		self.name = name
		self.solid = solid
		self.glyph = deepcopy(glyph)

		# If an entity is partially hidden, and thus unknown, show as a '?' but keep its colors.
		self.unknown_glyph = deepcopy(glyph)
		self.unknown_glyph.char = '?'
		# If an entity is partially hidden, and thus unknown, use the following as its name.
		self.unknown_name = "???"


	# Constants (overridden below due to Python limitations).
	PLAYER = None
	ORC = None


# Entity types (which serve as a base/template for spawning entities).

EntityType.PLAYER = EntityType(
	name = "Player",
	solid = True,
	glyph = Glyph('☻', Color.BLUE)
)

EntityType.ORC = EntityType(
	name = "Orc",
	solid = True,
	glyph = Glyph('o', Color.GREEN)
)
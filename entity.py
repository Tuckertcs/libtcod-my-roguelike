from entity_type import EntityType


class Entity:
	"""
	Represents a dynamic object with a position in world space.
	"""
	def __init__(
		self,
		type: EntityType, # The static template that this in-world entity represents.
		x: int = 0,
		y: int = 0
	):
		self.type = type

		self.x = x
		self.y = y
	

	def move(self, dx: int = 0, dy: int = 0):
		"""
		Move this Entity by the given relative amount.
		"""
		self.x += dx
		self.y += dy
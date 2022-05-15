from entity import Entity


class Game:
	"""
	The instance of a game that is played. Contains the world and all the maps and entities within, including the player, and is controlled externally through Commands.
	"""
	def __init__(self, player: Entity, seed: int = 0):
		self.player = player
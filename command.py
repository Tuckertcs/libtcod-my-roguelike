from entity import Entity
from game import Game


class Command:
	"""
	Commands do various tasks in a game. Any user input is translated from a tcod event to a Command, which then does whatever the input should've done within the game or to the window.
	Essentially, the EventHandler will read user input events, check them against control key bindings, and send a Command to be executed.
	For example, the EventHandler might read that the `W` key was pressed, and return a Command that would move the player up one tile.
	"""
	def execute(self) -> None:
		"""
		Virtual function that runs the command.
		"""
		raise NotImplementedError


class CloseWindowCommand(Command):
	def execute(self) -> None:
		raise SystemExit()


# Player movement.

class PlayerMoveUp(Command):
	def __init__(self, player: Entity):
		self.player = player
	

	def execute(self) -> None:
		self.player.move(0, -1)


class PlayerMoveDown(Command):
	def __init__(self, player: Entity):
		self.player = player
	

	def execute(self) -> None:
		self.player.move(0, 1)


class PlayerMoveLeft(Command):
	def __init__(self, player: Entity):
		self.player = player
	

	def execute(self) -> None:
		self.player.move(-1, 0)


class PlayerMoveRight(Command):
	def __init__(self, player: Entity):
		self.player = player
	

	def execute(self) -> None:
		self.player.move(1, 0)
import tcod

from game import Game
from tile_grid import TileGrid
from tile_type import TileType


class GameMap(TileGrid):
	"""
	A game map is TileGrid that exists within a Game, with Entities that interact in it, such as a dungeon or cave, an overworld map, etc.
	"""
	def __init__(
		self,
		game: Game,
		width: int = 256,
		height: int = 256,
		initial_tile_type: TileType = TileType.FLOOR
	):
		super().__init__(width, height, initial_tile_type)
		self.game = game
		self.player = game.player

		self.entities = []
	

	def render(self, console: tcod.Console) -> None:
		"""
		Render the GameMap's TileGrid and entities to the given console.
		"""
		self.render_tiles(console)
		self.render_entities(console)


	def render_entities(self, console: tcod.Console) -> None:
		"""
		Render the player and all other entities to the given console.
		"""
		# Print all entities as known (not unknown), for now.
		for entity in self.entities:
			entity_glyph = entity.type.glyph
			console.print(entity.x, entity.y, entity_glyph.char, entity_glyph.fg, entity_glyph.bg)

		# Print the player on top.
		player_glyph = self.player.type.glyph
		console.print(self.player.x, self.player.y, player_glyph.char, player_glyph.fg, player_glyph.bg)


	def render_tiles(self, console: tcod.console) -> None:
		"""
		Render the TileGrid to the given console.
		"""
		for x in range(self.get_width()):
			for y in range(self.get_height()):
				# Render all tiles as lit, for now.
				tile_glyph = self.get_tile(x, y).type.light_glyph
				console.print(x, y, tile_glyph.char, tile_glyph.fg, tile_glyph.bg)
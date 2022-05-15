from typing import Optional

from tile import Tile
from tile_type import TileType


class TileGrid:
	"""
	Represents a 2D grid of Tile objects.
	"""
	def __init__(
		self,
		width: int,
		height: int,
		initial_tile_type: TileType = TileType.FLOOR # The tile to fill this grid with, initially.
	):
		self._tiles = []
		for x in range(width):
			self._tiles.append([])
			for y in range(height):
				self._tiles[x].append(Tile(initial_tile_type))
	

	def get_width(self) -> int:
		return len(self._tiles)
	

	def get_height(self) -> int:
		return len(self._tiles[0])
	

	def in_bounds(self, x: int, y: int) -> bool:
		"""
		Return true if the given position is within this TileGrid's dimensions.
		"""
		return x >= 0 and y >= 0 and x < self.get_width() and y < self.get_height()
	

	def get_tile(self, x: int, y: int) -> Optional[Tile]:
		"""
		Return the tile at the given position.
		If the position is outside of this TileGrid's dimensions, return None instead.
		"""
		if self.in_bounds(x, y):
			return self._tiles[x][y]
		return None

	
	def set_tile(self, x: int, y: int, tile: Tile) -> Optional[Tile]:
		"""
		Set the tile at the given position.
		Returns the newly placed tile.
		If the position is outside of this TileGrid's dimensions, return None instead.
		"""
		if self.in_bounds(x, y):
			self._tiles[x][y] = tile
			return tile

		return None
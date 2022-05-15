from copy import deepcopy
from typing import Dict, List, Tuple

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
UP_LEFT = (-1, -1)
UP_RIGHT = (1, -1)
DOWN_LEFT = (-1, 1)
DOWN_RIGHT = (1, 1)
DIRS = [UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]


class Cell:
	def __init__(
		self,
		char: str,
		valid_up: List[str],
		valid_down: List[str],
		valid_left: List[str],
		valid_right: List[str],
		valid_up_left: List[str],
		valid_up_right: List[str],
		valid_down_left: List[str],
		valid_down_right: List[str],
	):
		self.char = char

		self.valid_neighbors = []
		self.valid_neighbors[UP] = valid_up
		self.valid_neighbors[DOWN] = valid_down
		self.valid_neighbors[LEFT] = valid_left
		self.valid_neighbors[RIGHT] = valid_right
		self.valid_neighbors[UP_LEFT] = valid_up_left
		self.valid_neighbors[UP_RIGHT] = valid_up_right
		self.valid_neighbors[DOWN_LEFT] = valid_down_left
		self.valid_neighbors[DOWN_RIGHT] = valid_down_right

		self.collapsed = False


ALL_CHARS = ['#', '.']
INITIAL_CELL = Cell(
	'?',
	deepcopy(ALL_CHARS),
	deepcopy(ALL_CHARS),
	deepcopy(ALL_CHARS),
	deepcopy(ALL_CHARS),
	deepcopy(ALL_CHARS),
	deepcopy(ALL_CHARS),
	deepcopy(ALL_CHARS),
	deepcopy(ALL_CHARS)
)


class WFC:
	def __init__(self, width: int, height: int):
		"""
		Create a wafe-function-collapse grid, and populate it with cells that allow any cell to be neighbors.
		"""
		self.width = width
		self.height = height

		self.grid = []
		for x in range(width):
			self.grid.append([])
			for y in range(height):
				self.grid[x].append(deepcopy(INITIAL_CELL))
	
	def run(self):
		# Collapse initial cell.

		while not self.is_collapsed():
			pass

	def is_collapsed(self):
		for x in self.width:
			for y in self.height:

from typing import  Tuple

from color import Color


class Glyph:
	"""
	A colored character that can be rendered to the console.
	"""
	def __init__(
		self,
		char: str = ' ',
		fg: Tuple[int, int, int] = Color.WHITE,
		bg: Tuple[int, int, int] = Color.BLACK
	):
		self.char = char
		self.fg = fg
		self.bg = bg
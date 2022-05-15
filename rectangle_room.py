from rectangle import Rect


class RectRoom(Rect):
	"""
	A rectangular area with 1-thick walls.
	"""
	def __init__(self, x: int, y: int, width: int, height: int):
		super().__init__(x, y, width, height)
		# The rectangle for just the inner area, excluding the 1-thick walls.
		self.inner = Rect(x + 1, y + 1, width - 2, height - 2)

class Rect:
	"""
	A basic rectangleular shape class.
	"""
	def __init__(self, x: int, y: int, width: int, height: int):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

		self.x1 = x
		self.y1 = y
		self.x2 = x + width
		self.y2 = y + height

		self.center_x = (self.x1 + self.x2) // 2
		self.center_y = (self.y1 + self.y2) // 2
	

	def in_bounds(self, x: int, y: int) -> bool:
		"""
		Return if a coordinate is within this rectangle's dimensions.
		"""
		return x >= self.x1 and y >= self.y1 and x <= self.x2 and y <= self.y2
	

	def overlaps(self, other: 'Rect') -> bool:
		"""
		Return if this rectangle is overlapping another rectangle.
		"""
		return self.x1 <= other.x2 and self.y1 <= other.y2 and self.x2 >= other.x1 and self.y2 >= other.y1
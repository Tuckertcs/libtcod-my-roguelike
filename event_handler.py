from typing import Optional

import tcod

from command import *
from game import Game


#ActionOrHandler = Union[Action, "BaseEventHandler"]
"""
An event handler return value which can trigger an action or switch active handlers.

If a handler is returned, it'll become the active handler for future events.
If an action is returned, it'll attempt to execute. If it's valid, MainGameEventHandler will become the active handler.
"""


#class BaseEventHandler(tcod.event.EventDispatch[ActionOrHandler]):
#	def handle_events(self, event: tcod.event.Event) -> 'BaseEventHandler':
#		pass

class EventHandler(tcod.event.EventDispatch[Optional[Command]]):
	"""
	Takes in and listens for tcod events, then returns a Command to be executed using `EventHandler.dispatch(Event)`.
	The returned Command may depend on the Game's state, i.e. the up arrow might return the command to move the player up, or it might move the selected item in an interface's list.
	"""
	def __init__(self, game: Game):
		self.game = game


	# Override.
	def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Command]:
		"""
		A key was pressed. 
		"""
		key = event.sym

		# Player movement.
		if key == tcod.event.K_UP:
			return PlayerMoveUp(self.game.player)
		elif key == tcod.event.K_DOWN:
			return PlayerMoveDown(self.game.player)
		elif key == tcod.event.K_LEFT:
			return PlayerMoveLeft(self.game.player)
		elif key == tcod.event.K_RIGHT:
			return PlayerMoveRight(self.game.player)

		return None
	

	# Override.
	def ev_keyup(self, event: tcod.event.KeyUp) -> Optional[Command]:
		"""
		A key was released.
		"""
		return None


	# Override.
	def ev_mousemotion(self, event: tcod.event.MouseMotion) -> Optional[Command]:
		"""
		The mouse cursor moved.
		"""
		return None
	

	# Override.
	def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[Command]:
		"""
		A mouse button was pressed.
		"""
		return None
	

	# Override.
	def ev_mousebuttonup(self, event: tcod.event.MouseButtonUp) -> Optional[Command]:
		"""
		A mouse button was released.
		"""
		return None
	

	# Override.
	def ev_mousewheel(self, event: tcod.event.MouseWheel) -> Optional[Command]:
		"""
		The mouse wheel was scrolled.
		"""
		return None
	

	# Override.
	def ev_textinput(self, event: tcod.event.TextInput) -> Optional[Command]:
		"""
		Unicode text was inputted.
		"""
		return None
	

	# Override.
	def ev_windowresized(self, event: tcod.event.WindowResized) -> Optional[Command]:
		"""
		The window was resized.
		"""
		return None

	# Override.
	def ev_windowsizechanged(self, event: tcod.event.WindowResized) -> Optional[Command]:
		"""
		The system or the user changed the window size.
		"""
		return None
	

	# Override.
	def ev_windowenter(self, event: tcod.event.WindowEvent) -> Optional[Command]:
		"""
		The window gained mouse focus.
		"""
		return None
	

	# Override.
	def ev_windowleave(self, event: tcod.event.WindowEvent) -> Optional[Command]:
		"""
		The window lost mouse focus.
		"""
		return None
	

	# Override.
	def ev_windowclose(self, event: tcod.event.WindowEvent) -> Optional[Command]:
		"""
		The window is requested to close (but not necessarily the entire program?).
		In our case, closing the window should always terminate the program too.
		"""
		return None
	

	# Override.
	def ev_quit(self, event: tcod.event.Quit) -> Optional[Command]:
		"""
		The program is requested to terminate, i.e. the window close button was clicked, or ALT+F4 (or similar) was pressed.
		"""
		return CloseWindowCommand()
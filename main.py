#!/usr/bin/env python3
from rectangle_room import RectRoom

import random

import tcod

from entity import Entity
from entity_type import EntityType
from event_handler import EventHandler
from game import Game
from game_map import GameMap
from tile_type import TileType


def main() -> None:
	"""
	Entry point.
	"""
	# Load the font.
	tileset = tcod.tileset.load_tilesheet("fonts/glifix-20x20.png", 16, 16, tcod.tileset.CHARMAP_CP437)

	# Create the window.
	context = tcod.context.new( # New window with pixel width and height
		width = 1920 // 2,
		height = 1080 // 2,
		tileset = tileset,
		title = "Roguelike",
		vsync = True,
		sdl_window_flags = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED,
	)

	# Temporary game stuff.
	game = Game(Entity(EntityType.PLAYER, 0, 0))
	game_map = GameMap(game, 512, 512, TileType.FLOOR)

	# Initialize event handling.
	event_handler = EventHandler(game)
	
	# Run the game loop.
	while True:
		# New root console, sized to fit screen.
		root_console = context.new_console(order="F")

		# Render the game.
		game_map.render(root_console)
		
		# Display final console.
		context.present(root_console, integer_scaling=True)

		# Wait for, and handle, events.
		for event in tcod.event.wait():
			context.convert_event(event) # Sets tile coordinates for mouse events.

			# If the event results in running a command, run it.
			command = event_handler.dispatch(event)
			if command:
				command.execute()
			

if __name__ == "__main__":
	main()
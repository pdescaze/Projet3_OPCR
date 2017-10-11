"""Module of the class Character"""
#!/usr/bin/python3
# -*- coding: Utf-8 -*

import json
import pygame
from pygame.locals import *
from content.constants import SPRITE_PER_SIDE, SPRITE_SIZE, PLAYER_SPRITE_SIZE, HALF_SPRITE
from content.structure import Structure

class Hero():
	""" Class for the hero. Permits to generate his position and load
	the hero picture at its right position. Also permits via movement method
	to move the hero inside the labyrinth with directional arrows"""
	def __init__(self, picture, file, main_window):
		self.picture = picture
		self.file = file
		self.main_window = main_window
		self.status = 0
		#Initialization of x and y of start position
		self.start_x = 0
		self.start_y = 0
		#Initialization of side x and y of the labyrinth window
		self.window_sidex = 0
		self.window_sidey = 0
		#Initialization of the player and its position
		self.position_player = ()
		self.player = 0
		#Initialization of the line number and the sprite number
		self.line_number_s = 0
		self.sprite_number_s = 0

		#Initialization of a Structure's object
		self.structure = Structure(self.file, self.main_window)

	def loading(self):
		""" method that permits to browse the "s" character representing the arrival
		in the .json file and then to load the hero picture at the start position"""
		for element in json.load(open(self.file)):
			for i in element:
				if i == "s":
					self.start_x, self.start_y = self.window_sidex, self.window_sidey
					self.sprite_number_s, self.line_number_s = int(self.window_sidex \
					 / SPRITE_SIZE), int(self.window_sidey / SPRITE_SIZE)
				self.window_sidex += SPRITE_SIZE
			self.window_sidex = 0
			self.window_sidey += SPRITE_SIZE

		self.player = pygame.image.load(self.picture).convert_alpha()
		self.player = pygame.transform.scale(self.player, (PLAYER_SPRITE_SIZE, \
			PLAYER_SPRITE_SIZE))
		self.position_player = self.player.get_rect(center=(self.start_x + HALF_SPRITE, \
			self.start_y + HALF_SPRITE))
		self.main_window.blit(self.player, self.position_player)
		pygame.display.flip()

	def movement(self, direction):
		""" This method permits to the hero to move following the key pressed.
		This method contains conditions such as collision with walls or out of limits
		positions. After a movement from the hero, this method permits to blit
		a sprite of field or start, following the nature of the previous sprite where
		the hero was"""
		structure = json.load(open(self.file))

		if direction == "up":
			#out of limits condition
			if self.line_number_s < 0:
				self.position_player = self.position_player.move(0, 0)
			else:
				#collision test with wall
				if structure[self.line_number_s - 1][self.sprite_number_s] != "w":
					self.position_player = self.position_player.move(0, -SPRITE_SIZE)
					#Test about the nature of the previous sprite
					if structure[self.line_number_s][self.sprite_number_s] == "s":
						self.structure.load_start(self.sprite_number_s, self.line_number_s)
					elif structure[self.line_number_s][self.sprite_number_s] == "O":
						self.structure.load_field(self.sprite_number_s, self.line_number_s)
					self.line_number_s -= 1

		elif direction == "down":
			if self.line_number_s >= len(structure) - 1:
				self.position_player = self.position_player.move(0, 0)
			else:
				if structure[self.line_number_s + 1][self.sprite_number_s] != "w":
					self.position_player = self.position_player.move(0, SPRITE_SIZE)
					if structure[self.line_number_s][self.sprite_number_s] == "s":
						self.structure.load_start(self.sprite_number_s, self.line_number_s)
					elif structure[self.line_number_s][self.sprite_number_s] == "O":
						self.structure.load_field(self.sprite_number_s, self.line_number_s)
					self.line_number_s += 1

		elif direction == "left":
			if self.sprite_number_s < 0:
				self.position_player = self.position_player.move(0, 0)
			else:
				if structure[self.line_number_s][self.sprite_number_s - 1] != "w":
					self.position_player = self.position_player.move(- SPRITE_SIZE, 0)
					if structure[self.line_number_s][self.sprite_number_s] == "s":
						self.structure.load_start(self.sprite_number_s, self.line_number_s)
					elif structure[self.line_number_s][self.sprite_number_s] == "O":
						self.structure.load_field(self.sprite_number_s, self.line_number_s)
					self.sprite_number_s -= 1

		elif direction == "right":
			if self.sprite_number_s > SPRITE_PER_SIDE - 1:
				self.position_player = self.position_player.move(0, 0)
			else:
				if structure[self.line_number_s][self.sprite_number_s + 1] != "w":
					self.position_player = self.position_player.move(SPRITE_SIZE, 0)
					if structure[self.line_number_s][self.sprite_number_s] == "s":
						self.structure.load_start(self.sprite_number_s, self.line_number_s)
					elif structure[self.line_number_s][self.sprite_number_s] == "O":
						self.structure.load_field(self.sprite_number_s, self.line_number_s)
					self.sprite_number_s += 1
		#Execution of the method load_frame of the class Structure.
		#That permits to refresh the adjacent frame
		self.structure.load_frame()
		self.structure.advices_play()
		self.structure.advices_quit()
		return self.position_player

	def test_position(self, position_guardian, \
		catch_item1, catch_item2, catch_item3):
		""" This method tests the collision between the hero and the guardian following
		the number of objects caught. If all the objects are caught, self.status=2
		else, self.status=1 """
		if self.position_player == position_guardian:
			if catch_item1 == False or catch_item2 == False or catch_item3 == False:
				self.status = 1
			else:
				self.status = 2
		else:
			pass
		return self.status

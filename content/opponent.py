""" Module about the opponent class"""
#!/usr/bin/python3
# -*- coding: Utf-8 -*

import json
import pygame
from pygame.locals import *
from content.constants import SPRITE_SIZE, PLAYER_SPRITE_SIZE, HALF_SPRITE

class Opponent():
	""" Class that permits to generate the position of the guardian following
	the labyrinth.json file and load the picture of the guardian at this position"""
	def __init__(self, picture, file, main_window):
		self.picture = picture
		self.file = file
		self.main_window = main_window
		#Initialization of x and y of arrival
		self.arrival_x = 0
		self.arrival_y = 0
		#Initialization of the side x and side y of the window
		self.window_sidex = 0
		self.window_sidey = 0
		#Initialiaztion of the position of the guardian
		self.position_guardian = ()
		self.guardian = 0

	def loading(self):
		"""This method permits to browse through the json file and search for
		the "a" character representing the arrival. It permits to update
		self.arrival_x and self.arrival_y and then to load the picture
		of the guardian at its right position on the main window"""
		for element in json.load(open(self.file)):
			for i in element:
				if i == "a":
					self.arrival_x, self.arrival_y = self.window_sidex, self.window_sidey
				self.window_sidex += SPRITE_SIZE
			self.window_sidex = 0
			self.window_sidey += SPRITE_SIZE

		self.guardian = pygame.image.load(self.picture).convert_alpha()
		self.guardian = pygame.transform.scale(self.guardian, (PLAYER_SPRITE_SIZE, \
			PLAYER_SPRITE_SIZE))
		self.position_guardian = self.guardian.get_rect(center=(self.arrival_x \
			+ HALF_SPRITE, self.arrival_y + HALF_SPRITE))
		self.main_window.blit(self.guardian, self.position_guardian)
		pygame.display.flip()

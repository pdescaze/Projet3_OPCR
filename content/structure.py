""" Module of the class Structure """
#!/usr/bin/python3
# -*- coding: Utf-8 -*

import json
import pygame
from pygame.locals import *
from content.constants import *


class Structure():
	""" Class that permits to generate and load the labyrinth, the adjacent
 	frame and the inventory via methods"""
	def __init__(self, file, main_window):
		self.file = file
		self.main_window = main_window
		#Initialization of the window side
		self.window_sidex = 0
		self.window_sidey = 0
		#Initialization of start/arrival x and y
		self.start_x = 0
		self.start_y = 0
		self.arrival_x = 0
		self.arrival_y = 0
		#Initialization of line_number and sprite_number
		self.line_number = 0
		self.sprite_number = 0
		#Initialization of cropped parts of floors.png
		self.cropped_wall = 0
		self.cropped_start = 0
		self.cropped_field = 0
		self.cropped_arrival = 0
		

	def loading(self):
		""" method that permits to browse self.file and identify every character
		of every line. Following the character, it will load the right picture.
		This method browses one character after the other, line after line"""
		for element in json.load(open(self.file)):
			for i in element:
				if i == "w":
					#loading background_picture picture (picture of all backgrounds)
					background = pygame.image.load(BACKGROUND_PICTURE).convert()
					#select and assign the right picture to the character
					self.cropped_wall = background.subsurface(BACKGROUND_WALL)
					#transform the scale of the picture (40x40 pixels)
					self.cropped_wall = pygame.transform.scale(self.cropped_wall, (SPRITE_SIZE, \
						SPRITE_SIZE))
					#blit the selected picture in the main window
					self.main_window.blit(self.cropped_wall, (self.window_sidex, self.window_sidey))
				elif i == "a":
					background = pygame.image.load(BACKGROUND_PICTURE).convert()
					self.cropped_arrival = background.subsurface(BACKGROUND_ARRIVAL)
					self.cropped_arrival = pygame.transform.scale(self.cropped_arrival, (SPRITE_SIZE, \
						SPRITE_SIZE))
					self.main_window.blit(self.cropped_arrival, (self.window_sidex, self.window_sidey))
					#Obtaining arrival_x and arrival_y
					self.arrival_x, self.arrival_y = self.window_sidex, self.window_sidey
				elif i == "s":
					background = pygame.image.load(BACKGROUND_PICTURE).convert()
					self.cropped_start = background.subsurface(BACKGROUND_START)
					self.cropped_start = pygame.transform.scale(self.cropped_start, (SPRITE_SIZE, \
						SPRITE_SIZE))
					self.main_window.blit(self.cropped_start, (self.window_sidex, self.window_sidey))
					#Obtaining start_x and start_y
					self.start_x, self.start_y = self.window_sidex, self.window_sidey
				elif i == "O":
					background = pygame.image.load(BACKGROUND_PICTURE).convert()
					self.cropped_field = background.subsurface(BACKGROUND_FIELD)
					self.cropped_field = pygame.transform.scale(self.cropped_field, (SPRITE_SIZE, \
						SPRITE_SIZE))
					self.main_window.blit(self.cropped_field, (self.window_sidex, self.window_sidey))
				self.window_sidex += SPRITE_SIZE
				pygame.display.flip()
			self.window_sidex = 0
			self.window_sidey += SPRITE_SIZE
			pygame.display.flip()

	def load_field(self, sprite_number_s, line_number_s):
		""" This method permits to load the field picture on the previous
		sprite location of the hero after a movement"""
		background = pygame.image.load(BACKGROUND_PICTURE).convert()
		self.cropped_field = background.subsurface(BACKGROUND_FIELD)
		self.cropped_field = pygame.transform.scale(self.cropped_field, (SPRITE_SIZE, \
			SPRITE_SIZE))
		self.main_window.blit(self.cropped_field, (sprite_number_s \
			* SPRITE_SIZE, line_number_s * SPRITE_SIZE))

	def load_start(self, sprite_number_s, line_number_s):
		""" This method permits to load the start picture on the previous
		sprite location of the hero after a movement"""
		background = pygame.image.load(BACKGROUND_PICTURE).convert()
		self.cropped_start = background.subsurface(BACKGROUND_START)
		self.cropped_start = pygame.transform.scale(self.cropped_start, (SPRITE_SIZE, \
			SPRITE_SIZE))
		self.main_window.blit(self.cropped_start, (sprite_number_s \
			* SPRITE_SIZE, line_number_s * SPRITE_SIZE))

	def load_frame(self):
		""" This methis permits to load an adjacent frame of the main
		labyrinth structure. This frame load a black background and
		contain the title of the game """
		self.frame_background = pygame.image.load(BACKGROUND_FRAME).convert()
		self.frame_background = pygame.transform.scale(self.frame_background, \
			(WINDOW_SIDE_X - FRAME_SIDE_X, WINDOW_SIDE_Y))
		self.main_window.blit(self.frame_background, (FRAME_SIDE_X, 0))
		self.frame = pygame.font.SysFont("monospace", 30)
		self.frame_display = self.frame.render("McGyver Escape", 1, (255, 255, 0))
		self.main_window.blit(self.frame_display, TITLE_DISPLAY_POSITION)

	def advices_play(self):
		"""Method that blit advices to Quit the game"""
		self.frame_advice_play = pygame.font.SysFont("monospace", 20)
		self.frame_advice_play_display = self.frame_advice_play.render(\
			"To PLAY: Use Directional Arrows", 1, (255, 0, 0))
		self.main_window.blit(self.frame_advice_play_display, ADVICE_PLAY_DISPLAY_POSITION)

	def advices_quit(self):
		"""Method that blit advices to Quit the game"""
		self.frame_advice_quit = pygame.font.SysFont("monospace", 20)
		self.frame_advice_quit_display = self.frame_advice_quit.render(\
			"To QUIT : Press Red Cross ", 1, (255, 0, 0))
		self.main_window.blit(self.frame_advice_quit_display, ADVICE_QUIT_DISPLAY_POSITION)

		self.frame_advice2_quit = pygame.font.SysFont("monospace", 20)
		self.frame_advice2_quit_display = self.frame_advice2_quit.render(\
			"or Escape Key", 1, (255, 0, 0))
		self.main_window.blit(self.frame_advice2_quit_display, ADVICE2_QUIT_DISPLAY_POSITION)

	def load_victory(self, victory_picture):
		""" This method permits to load the victory picture, available only if
		self.status == 2 """
		self.victory_picture = pygame.image.load(victory_picture).convert()
		self.victory_picture.set_colorkey((255, 255, 255))
		self.victory_picture = pygame.transform.scale(self.victory_picture, (FRAME_SIDE_X, \
			WINDOW_SIDE_Y))
		self.main_window.blit(self.victory_picture, (0, 0))
		self.main_window.blit(self.cropped_arrival, (self.arrival_x, self.arrival_y))

	def load_defeat(self, defeat_picture, artwork):
		""" This method permits to load the defeat picture, available only if
		self.status == 1 and the blood picture representing the death of
		the hero """
		self.defeat_picture = pygame.image.load(defeat_picture).convert()
		self.defeat_picture.set_colorkey((255, 255, 255))
		self.defeat_picture = pygame.transform.scale(self.defeat_picture, (FRAME_SIDE_X,\
			WINDOW_SIDE_Y))
		self.main_window.blit(self.defeat_picture, (0, 0))

		self.pick_blood_picture = pygame.image.load(artwork).convert_alpha()
		self.blood_picture = self.pick_blood_picture.subsurface(ARTWORK_BLOOD)
		self.blood_picture = pygame.transform.scale(self.blood_picture, (OBJECT_SPRITE_SIZE,\
			OBJECT_SPRITE_SIZE))
		self.main_window.blit(self.cropped_arrival, (self.arrival_x, self.arrival_y))
		self.main_window.blit(self.blood_picture, (self.arrival_x, self.arrival_y))
		

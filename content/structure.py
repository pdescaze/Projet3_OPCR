#!/usr/bin/python3
# -*- coding: Utf-8 -*

import os
import sys
import json
import pygame
from pygame.locals import *
from content.constants import *


class Structure():
	""" Class that permits to generate and load the labyrinth, the adjacent
 	frame and the inventory via methods"""
	def __init__(self,file,main_window):
		self.file = file
		self.main_window=main_window
		self.status=0		
		#Initialization of the window side
		self.window_sidex=0
		self.window_sidey=0
		#Initialization of start x and y
		self.start_x=0
		self.start_y=0
		#Initialization of line_number and sprite_number	
		self.line_number=0
		self.sprite_number=0

	def loading(self):
		""" method that permits to browse self.file and identify every character 
		of every line. Following the character, it will load the right picture. 
		This method browses one character after the other, line after line"""	
		for element in json.load(open(self.file)):
			for i in element:
				if i == "w":
					#loading background_picture picture (picture of all backgrounds)
					background=pygame.image.load(background_picture).convert()
					#select and assign the right picture to the character	
					self.cropped_wall=background.subsurface(background_wall)
					#transform the scale of the picture (40x40 pixels)	
					self.cropped_wall=pygame.transform.scale(self.cropped_wall,(sprite_size,
						sprite_size))
					#blit the selected picture in the main window
					self.main_window.blit(self.cropped_wall,(self.window_sidex,self.window_sidey))
				elif i == "a":
					background=pygame.image.load(background_picture).convert()
					self.cropped_arrival=background.subsurface(background_arrival)
					self.cropped_arrival=pygame.transform.scale(self.cropped_arrival,(sprite_size,
						sprite_size))
					self.main_window.blit(self.cropped_arrival,(self.window_sidex,self.window_sidey))
					#Obtaining arriva_x and arrival_y
					self.arrival_x,self.arrival_y=self.window_sidex,self.window_sidey
				elif i == "s":
					background=pygame.image.load(background_picture).convert()
					self.cropped_start=background.subsurface(background_start)
					self.cropped_start=pygame.transform.scale(self.cropped_start,(sprite_size,
						sprite_size))
					self.main_window.blit(self.cropped_start,(self.window_sidex,self.window_sidey))
					#Obtaining start_x and start_y
					self.start_x,self.start_y=self.window_sidex,self.window_sidey					
				elif i == "O":
					background=pygame.image.load(background_picture).convert()
					self.cropped_field=background.subsurface(background_field)
					self.cropped_field=pygame.transform.scale(self.cropped_field,(sprite_size,
						sprite_size))
					self.main_window.blit(self.cropped_field,(self.window_sidex,self.window_sidey))
				self.window_sidex += sprite_size
				pygame.display.flip()
			self.window_sidex=0
			self.window_sidey+=sprite_size
			pygame.display.flip()

	def load_field(self,sprite_number_s,line_number_s):
		""" This method permits to load the field picture on the previous 
		sprite location of the hero after a movement"""
		background=pygame.image.load(background_picture).convert()
		self.cropped_field=background.subsurface(background_field)
		self.cropped_field=pygame.transform.scale(self.cropped_field,(sprite_size,
			sprite_size))
		self.main_window.blit(self.cropped_field,(sprite_number_s 
			* sprite_size,line_number_s * sprite_size))		
	
	def load_start(self,sprite_number_s,line_number_s):
		""" This method permits to load the start picture on the previous 
		sprite location of the hero after a movement"""
		background=pygame.image.load(background_picture).convert()	
		self.cropped_start=background.subsurface(background_start)
		self.cropped_start=pygame.transform.scale(self.cropped_start,(sprite_size,
			sprite_size))
		self.main_window.blit(self.cropped_start,(sprite_number_s 
			* sprite_size,line_number_s * sprite_size))
	
	def load_frame(self):
		""" This methis permits to load an adjacent frame of the main
		labyrinth structure. This frame load a black background and
		contain the title of the game """
		self.frame_background=pygame.image.load(background_frame).convert()
		self.frame_background=pygame.transform.scale(self.frame_background,
			(window_side_x - frame_side_x,window_side_y))
		self.main_window.blit(self.frame_background,(frame_side_x,0))
		self.frame = pygame.font.SysFont("monospace", 30)
		self.frame_display = self.frame.render("McGyver Escape", 1, (255,255,0))
		self.main_window.blit(self.frame_display, title_display_position)

	def advices_play(self):
		"""Method that blit advices to Quit the game"""
		self.frame_advice_play = pygame.font.SysFont("monospace",20)
		self.frame_advice_play_display = self.frame_advice_play.render(
			"To PLAY: Use Directional Arrows", 1, (255,0,0))
		self.main_window.blit(self.frame_advice_play_display, advice_play_display_position)

	def advices_quit(self):
		"""Method that blit advices to Quit the game"""
		self.frame_advice = pygame.font.SysFont("monospace", 20)
		self.frame_advice_display = self.frame_advice.render(
			"To QUIT : Press Red Cross ", 1, (255,0,0))
		self.main_window.blit(self.frame_advice_display, advice_display_position)

		self.frame_advice2 = pygame.font.SysFont("monospace", 20)
		self.frame_advice2_display = self.frame_advice2.render(
			"or Escape Key", 1, (255,0,0))
		self.main_window.blit(self.frame_advice2_display, advice2_display_position)

	def test_position(self,position_player,position_guardian,
		catch_item1,catch_item2,catch_item3):
		""" This method tests the collision between the hero and the guardian following
		the number of objects caught. If all the objects are caught, self.status=2
		else, self.status=1 """
		if position_player == position_guardian:
			if catch_item1 == False or catch_item2 == False or catch_item3 == False:
				self.status=1
			else:
				self.status=2
		else:
			pass
		return self.status
	
	def load_victory(self,victory_picture):
		""" This method permits to load the victory picture, available only if 
		self.status == 2 """
		self.victory_picture=pygame.image.load(victory_picture).convert()
		self.victory_picture.set_colorkey((255,255,255))
		self.victory_picture=pygame.transform.scale(self.victory_picture,(frame_side_x,
			window_side_y))
		self.main_window.blit(self.victory_picture,(0,0))
		self.main_window.blit(self.cropped_arrival,(self.arrival_x,self.arrival_y))
		
	def load_defeat(self,defeat_picture,artwork):
		""" This method permits to load the defeat picture, available only if 
		self.status == 1 and the blood picture representing the death of 
		the hero """
		self.defeat_picture=pygame.image.load(defeat_picture).convert()
		self.defeat_picture.set_colorkey((255,255,255))
		self.defeat_picture=pygame.transform.scale(self.defeat_picture,(frame_side_x,
			window_side_y))
		self.main_window.blit(self.defeat_picture,(0,0))

		self.pick_blood_picture=pygame.image.load(artwork).convert_alpha()
		self.blood_picture=self.pick_blood_picture.subsurface(artwork_blood)
		self.blood_picture=pygame.transform.scale(self.blood_picture,(object_sprite_size,
			object_sprite_size))
		self.main_window.blit(self.cropped_arrival,(self.arrival_x,self.arrival_y))
		self.main_window.blit(self.blood_picture,(self.arrival_x,self.arrival_y))





		
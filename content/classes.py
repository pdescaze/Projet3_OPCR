#!/usr/bin/python3
# -*- coding: Utf-8 -*

import os
import sys
import json
import pygame
from pygame.locals import *
from random import randrange


from constants import *
from classes import *


class Structure():

	
	def __init__(self,file):
		self.file = file
		self.window_sidex=0
		self.window_sidex=0
		self.start_x=0
		self.start_y=0
		self.window_sidex=0
		self.window_sidey=0


	def loading(self,main_window):

		
		for element in json.load(open(self.file)):
			for i in element:
				if i == "w":
					background=pygame.image.load(background_picture).convert()	#téléchargement de la plaquette d'image floors.png
					cropped_wall=background.subsurface(background_wall)			#sélection et assignation de l'image wall issue de l'image floors
					cropped_wall=pygame.transform.scale(cropped_wall,(sprite_size,sprite_size))		#transformation de l'échelle (40x40 pixels)
					main_window.blit(cropped_wall,(self.window_sidex,self.window_sidey))	#collage de l'image wall sur la fenetre principale.
				elif i == "a":
					background=pygame.image.load(background_picture).convert()
					cropped_arrival=background.subsurface(background_arrival)
					cropped_arrival=pygame.transform.scale(cropped_arrival,(sprite_size,sprite_size))
					main_window.blit(cropped_arrival,(self.window_sidex,self.window_sidey))
					self.arrival_x,self.arrival_y=self.window_sidex,self.window_sidey
				elif i == "s":
					background=pygame.image.load(background_picture).convert()
					cropped_start=background.subsurface(background_start)
					cropped_start=pygame.transform.scale(cropped_start,(sprite_size,sprite_size))
					main_window.blit(cropped_start,(self.window_sidex,self.window_sidey))
					self.start_x,self.start_y=self.window_sidex,self.window_sidey
				elif i == "O":
					background=pygame.image.load(background_picture).convert()
					cropped_field=background.subsurface(background_field)
					cropped_field=pygame.transform.scale(cropped_field,(sprite_size,sprite_size))
					main_window.blit(cropped_field,(self.window_sidex,self.window_sidey))
				self.window_sidex += sprite_size
				pygame.display.flip()
			self.window_sidex=0
			self.window_sidey+=sprite_size




class Character():

	def __init__(self,picture,file):
		self.picture=picture
		self.file=file
		self.start_x=0
		self.start_y=0
		self.window_sidex=0
		self.window_sidey=0
		self.position_player=()	
		self.player=0

	def loading(self,main_window):

	
		for element in json.load(open(self.file)):
			for i in element:
				if i == "s":
					self.start_x,self.start_y=self.window_sidex,self.window_sidey
				self.window_sidex+=sprite_size
			self.window_sidex=0
			self.window_sidey+=sprite_size	

		self.player = pygame.image.load(self.picture).convert_alpha()
		self.player = pygame.transform.scale(self.player, (player_sprite_size, player_sprite_size))
		self.position_player=self.player.get_rect(center = (self.start_x +20 ,self.start_y +20))
		main_window.blit(self.player,self.position_player)
		pygame.display.flip()


	def movement(self,direction):
		
		
		if direction == "up":	
			self.position_player=self.position_player.move(0,-40)
		   	
		elif direction == "down":
			self.position_player=self.position_player.move(0,40)
		   
		elif direction == "left":
			self.position_player=self.position_player.move(-40,0)
		   
		elif direction == "right":			
		    self.position_player=self.position_player.move(40,0)

		

		

class Opponent():

	def __init__(self,picture,file):
		self.picture=picture
		self.file=file
		self.arrival_x=0
		self.arrival_y=0
		self.window_sidex=0
		self.window_sidey=0
		self.position_player=()	
		self.player=0


	def loading(self,main_window):

		
		for element in json.load(open(self.file)):
			for i in element:
				if i == "a":
					self.arrival_x,self.arrival_y=self.window_sidex,self.window_sidey
				self.window_sidex+=sprite_size
			self.window_sidex=0
			self.window_sidey+=sprite_size	

		self.player = pygame.image.load(self.picture).convert_alpha()
		self.player = pygame.transform.scale(self.player, (player_sprite_size, player_sprite_size))
		self.position_player=self.player.get_rect(center = (self.arrival_x +20 ,self.arrival_y +20))
		main_window.blit(self.player,self.position_player)
		pygame.display.flip()






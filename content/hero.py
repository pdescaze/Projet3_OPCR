#!/usr/bin/python3
# -*- coding: Utf-8 -*

import os
import sys
import json
import pygame
from pygame.locals import *



from content.constants import *
from content.structure import Structure



class Character():

	def __init__(self,picture,file,main_window):
		self.picture=picture
		self.file=file
		self.main_window=main_window
		self.start_x=0
		self.start_y=0
		self.window_sidex=0
		self.window_sidey=0
		self.position_player=()	
		self.player=0
		self.ligne_number_s=0
		self.sprite_number_s=0

		""" Initialization of object """
		self.structure=Structure(self.file,self.main_window)
		
		
		
	def loading(self):
		""" method that permits to load hero picture at the start position"""
	
		for element in json.load(open(self.file)):
			for i in element:
				if i == "s":
					self.start_x,self.start_y=self.window_sidex,self.window_sidey
					self.sprite_number_s,self.ligne_number_s=int(self.window_sidex/sprite_size),int(self.window_sidey/sprite_size)
				self.window_sidex+=sprite_size
			self.window_sidex=0
			self.window_sidey+=sprite_size	

		self.player = pygame.image.load(self.picture).convert_alpha()
		self.player = pygame.transform.scale(self.player, (player_sprite_size, player_sprite_size))
		self.position_player=self.player.get_rect(center = (self.start_x + half_sprite ,self.start_y + half_sprite))
		self.main_window.blit(self.player,self.position_player)
		pygame.display.flip()
		

	def movement(self,direction):
		
		structure=json.load(open(self.file))
	
	
		if direction == "up":
			if self.ligne_number_s < 0 :
				self.position_player=self.position_player.move(0,0)
			else:
				if structure[self.ligne_number_s-1][self.sprite_number_s] != "w":
					self.position_player=self.position_player.move(0,-sprite_size)
					if structure [self.ligne_number_s][self.sprite_number_s] == "s":
						self.structure.load_start(self.sprite_number_s,self.ligne_number_s)
					elif structure[self.ligne_number_s][self.sprite_number_s] == "O":
						self.structure.load_field(self.sprite_number_s,self.ligne_number_s)
					self.ligne_number_s-=1
			

		elif direction == "down":
			if self.ligne_number_s >= len(structure)-1:
				self.position_player=self.position_player.move(0,0)
			else:
				if structure[self.ligne_number_s+1][self.sprite_number_s] != "w":
					self.position_player=self.position_player.move(0,sprite_size)
					if structure [self.ligne_number_s][self.sprite_number_s] == "s":
						self.structure.load_start(self.sprite_number_s,self.ligne_number_s)
					elif structure[self.ligne_number_s][self.sprite_number_s] == "O":
						self.structure.load_field(self.sprite_number_s,self.ligne_number_s)
					self.ligne_number_s +=1
		   	

		elif direction == "left":
			if self.sprite_number_s < 0:
				self.position_player=self.position_player.move(0,0)
			else:
				if structure[self.ligne_number_s][self.sprite_number_s-1] != "w":
					self.position_player=self.position_player.move(-sprite_size,0)
					if structure [self.ligne_number_s][self.sprite_number_s] == "s":
						self.structure.load_start(self.sprite_number_s,self.ligne_number_s)
					elif structure[self.ligne_number_s][self.sprite_number_s] == "O":
						self.structure.load_field(self.sprite_number_s,self.ligne_number_s)
					self.sprite_number_s -=1
			

		elif direction == "right":	
			if self.sprite_number_s > sprite_per_side -1:
				self.position_player=self.position_player.move(0,0)
			else:
				if structure[self.ligne_number_s][self.sprite_number_s+1] != "w":
					self.position_player=self.position_player.move(sprite_size,0)
					if structure [self.ligne_number_s][self.sprite_number_s] == "s":
						self.structure.load_start(self.sprite_number_s,self.ligne_number_s)
					elif structure[self.ligne_number_s][self.sprite_number_s] == "O":
						self.structure.load_field(self.sprite_number_s,self.ligne_number_s)
					self.sprite_number_s +=1
		
		self.structure.load_frame()	
		

		return self.position_player


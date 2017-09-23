#!/usr/bin/python3
# -*- coding: Utf-8 -*

import os
import sys
import json
import pygame
from pygame.locals import *
from random import randint


from content.constants import *



	

class Opponent():

	def __init__(self,picture,file,main_window):
		self.picture=picture
		self.file=file
		self.main_window=main_window
		self.arrival_x=0
		self.arrival_y=0
		self.window_sidex=0
		self.window_sidey=0
		self.position_guardian=()	
		self.guardian=0


	def loading(self):

		
		for element in json.load(open(self.file)):
			for i in element:
				if i == "a":
					self.arrival_x,self.arrival_y=self.window_sidex,self.window_sidey
				self.window_sidex+=sprite_size
			self.window_sidex=0
			self.window_sidey+=sprite_size	

		self.guardian = pygame.image.load(self.picture).convert_alpha()
		self.guardian = pygame.transform.scale(self.guardian, (player_sprite_size, player_sprite_size))
		self.position_guardian=self.guardian.get_rect(center = (self.arrival_x +half_sprite ,self.arrival_y +half_sprite))
		self.main_window.blit(self.guardian,self.position_guardian)
		pygame.display.flip()

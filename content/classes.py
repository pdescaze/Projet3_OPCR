#!/usr/bin/python3
# -*- coding: Utf-8 -*

import os
import sys
import json
import pygame
from pygame.locals import *
from random import randint


from content.constants import *


class Structure():

	
	def __init__(self,file):
		self.file = file
		self.window_sidex=0
		self.window_sidex=0
		self.start_x=0
		self.start_y=0
		self.window_sidex=0
		self.window_sidey=0
		self.ligne_number=0
		self.sprite_number=0
		self.cropped_start=""
		self.cropped_field=""


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
		self.ligne_number_s=0
		self.sprite_number_s=0
		
		
	def loading(self,main_window):

	
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
		main_window.blit(self.player,self.position_player)
		pygame.display.flip()
		

	def movement(self,direction,main_window):
		
		structure=json.load(open(self.file))
		background=pygame.image.load(background_picture).convert()		

		if direction == "up":
			if self.ligne_number_s < 0 :
				self.position_player=self.position_player.move(0,0)
			else:
				if structure[self.ligne_number_s-1][self.sprite_number_s] != "w":
					self.position_player=self.position_player.move(0,-sprite_size)
					if structure [self.ligne_number_s][self.sprite_number_s] == "s":
						self.cropped_start=background.subsurface(background_start)
						self.cropped_start=pygame.transform.scale(self.cropped_start,(sprite_size,sprite_size))
						main_window.blit(self.cropped_start,(self.sprite_number_s * sprite_size,self.ligne_number_s * sprite_size))
					elif structure[self.ligne_number_s][self.sprite_number_s] == "O":
						self.cropped_field=background.subsurface(background_field)
						self.cropped_field=pygame.transform.scale(self.cropped_field,(sprite_size,sprite_size))
						main_window.blit(self.cropped_field,(self.sprite_number_s * sprite_size,self.ligne_number_s * sprite_size))
					self.ligne_number_s-=1

		elif direction == "down":
			if self.ligne_number_s >= len(structure)-1:
				self.position_player=self.position_player.move(0,0)
			else:
				if structure[self.ligne_number_s+1][self.sprite_number_s] != "w":
					self.position_player=self.position_player.move(0,sprite_size)
					if structure [self.ligne_number_s][self.sprite_number_s] == "s":
						self.cropped_start=background.subsurface(background_start)
						self.cropped_start=pygame.transform.scale(self.cropped_start,(sprite_size,sprite_size))
						main_window.blit(self.cropped_start,(self.sprite_number_s * sprite_size,self.ligne_number_s * sprite_size))
					elif structure[self.ligne_number_s][self.sprite_number_s] == "O":
						self.cropped_field=background.subsurface(background_field)
						self.cropped_field=pygame.transform.scale(self.cropped_field,(sprite_size,sprite_size))
						main_window.blit(self.cropped_field,(self.sprite_number_s * sprite_size,self.ligne_number_s * sprite_size))
					self.ligne_number_s +=1
		   
		elif direction == "left":
			if self.sprite_number_s < 0:
				self.position_player=self.position_player.move(0,0)
			else:
				if structure[self.ligne_number_s][self.sprite_number_s-1] != "w":
					self.position_player=self.position_player.move(-sprite_size,0)
					if structure [self.ligne_number_s][self.sprite_number_s] == "s":
						self.cropped_start=background.subsurface(background_start)
						self.cropped_start=pygame.transform.scale(self.cropped_start,(sprite_size,sprite_size))
						main_window.blit(self.cropped_start,(self.sprite_number_s * sprite_size,self.ligne_number_s * sprite_size))
					elif structure[self.ligne_number_s][self.sprite_number_s] == "O":
						self.cropped_field=background.subsurface(background_field)
						self.cropped_field=pygame.transform.scale(self.cropped_field,(sprite_size,sprite_size))
						main_window.blit(self.cropped_field,(self.sprite_number_s * sprite_size,self.ligne_number_s * sprite_size))
					self.sprite_number_s -=1

		elif direction == "right":	
			if self.sprite_number_s > sprite_per_side -1:
				self.position_player=self.position_player.move(0,0)
			else:
				if structure[self.ligne_number_s][self.sprite_number_s+1] != "w":
					self.position_player=self.position_player.move(sprite_size,0)
					if structure [self.ligne_number_s][self.sprite_number_s] == "s":
						self.cropped_start=background.subsurface(background_start)
						self.cropped_start=pygame.transform.scale(self.cropped_start,(sprite_size,sprite_size))
						main_window.blit(self.cropped_start,(self.sprite_number_s * sprite_size,self.ligne_number_s * sprite_size))
					elif structure[self.ligne_number_s][self.sprite_number_s] == "O":
						self.cropped_field=background.subsurface(background_field)
						self.cropped_field=pygame.transform.scale(self.cropped_field,(sprite_size,sprite_size))
						main_window.blit(self.cropped_field,(self.sprite_number_s * sprite_size,self.ligne_number_s * sprite_size))
					self.sprite_number_s +=1
				



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
		self.position_player=self.player.get_rect(center = (self.arrival_x +half_sprite ,self.arrival_y +half_sprite))
		main_window.blit(self.player,self.position_player)
		pygame.display.flip()






class Object():

	def __init__(self,file,object1,object2,object3,main_window):
		self.file=file
		self.object1=object1
		self.object2=object2
		self.object3=object3
		self.main_window=main_window
		self.proceed=1
		self.test_object1,self.test_object2,self.test_object3=False,False,False
		self.test_item1,self.test_item2,self.test_item3=False,False,False

	def generate(self):

		structure=json.load(open(self.file))

		while self.proceed:

			self.ligne_number=randint(0,len(structure)-1)
			self.sprite_number=randint(0,sprite_per_side-1)
			self.ligne_number2=randint(0,len(structure)-1)
			self.sprite_number2=randint(0,sprite_per_side-1)
			self.ligne_number3=randint(0,len(structure)-1)
			self.sprite_number3=randint(0,sprite_per_side-1)
			self.test_item1,self.test_item2,self.test_item3=False,False,False

			if structure[self.ligne_number][self.sprite_number] != "O":
				self.test_item1=False
			else:
				self.test_item1=True

			if self.ligne_number2 != self.ligne_number or self.ligne_number2 == self.ligne_number and self.sprite_number2 != self.sprite_number:
				if structure[self.ligne_number2][self.sprite_number2] != "O":	
					self.test_item2=False
				else:
					self.test_item2=True

			if self.ligne_number3 != self.ligne_number and self.ligne_number3 != self.ligne_number2 or self.ligne_number3 == self.ligne_number and self.sprite_number3 != self.sprite_number or self.ligne_number3 == self.ligne_number2 and self.sprite_number3 != self.sprite_number2:
				if structure[self.ligne_number3][self.sprite_number3] != "O":
					self.test_item3=False
				else:
					self.test_item3=True

			if self.test_item1 == True and self.test_item2==True and self.test_item3==True:
				self.proceed=0

	
	def loading(self,main_window):

			if self.test_item1 == True : 
				self.item1=pygame.image.load(self.object1).convert_alpha()		
				self.item1=pygame.transform.scale(self.item1,(object_sprite_size,object_sprite_size))
				self.position_item1=self.item1.get_rect(center=(self.sprite_number *sprite_size + half_sprite,self.ligne_number*sprite_size+half_sprite))
				main_window.blit(self.item1,self.position_item1)
			else:
				pass

			if self.test_item2 == True:
				self.item2=pygame.image.load(self.object2).convert_alpha()
				self.item2=pygame.transform.scale(self.item2,(object_sprite_size,object_sprite_size))												
				self.position_object2=self.item2.get_rect(center=(self.sprite_number2 *sprite_size + half_sprite,self.ligne_number2*sprite_size+half_sprite))
				main_window.blit(self.item2,self.position_object2)
			else:
				pass

			if self.test_item3 == True:
				self.item3=pygame.image.load(self.object3).convert_alpha()
				self.item3=pygame.transform.scale(self.item3,(object_sprite_size,object_sprite_size))												
				self.position_object3=self.item3.get_rect(center=(self.sprite_number3 *sprite_size + half_sprite,self.ligne_number3*sprite_size+half_sprite))
				main_window.blit(self.item3,self.position_object3)
			else:
				pass

			pygame.display.flip()
				




#!/usr/bin/python3
# -*- coding: Utf-8 -*

import os
import sys
import json
import pygame
from pygame.locals import *
from random import randint


from content.constants import *



class Object():

	def __init__(self,artwork,object3,file,main_window):
		self.file=file
		self.artwork=artwork 	#object1 and object2
		self.object3=object3
		self.main_window=main_window
		self.proceed=1
		self.test_item1,self.test_item2,self.test_item3=False,False,False
		self.item_inventory=[]
		self.catch_item1,self.catch_item2,self.catch_item3=False,False,False


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


	
	def loading(self):

			if self.test_item1 == True : 
				self.pick_item1=pygame.image.load(self.artwork).convert_alpha()
				self.item1=self.pick_item1.subsurface(artwork_object1)
				self.item1=pygame.transform.scale(self.item1,(object_sprite_size,object_sprite_size))
				self.position_item1=self.item1.get_rect(center=(self.sprite_number *sprite_size + half_sprite,self.ligne_number*sprite_size+half_sprite))
				self.main_window.blit(self.item1,self.position_item1)
			else:
				pass

			if self.test_item2 == True:
				self.pick_item2=pygame.image.load(self.artwork).convert_alpha()
				self.item2=self.pick_item2.subsurface(artwork_object2)
				self.item2=pygame.transform.scale(self.item2,(object_sprite_size,object_sprite_size))												
				self.position_item2=self.item2.get_rect(center=(self.sprite_number2 *sprite_size + half_sprite,self.ligne_number2*sprite_size+half_sprite))
				self.main_window.blit(self.item2,self.position_item2)
			else:
				pass

			if self.test_item3 == True:
				self.item3=pygame.image.load(self.object3).convert_alpha()
				self.item3=pygame.transform.scale(self.item3,(object_sprite_size,object_sprite_size))												
				self.position_item3=self.item3.get_rect(center=(self.sprite_number3 *sprite_size + half_sprite,self.ligne_number3*sprite_size+half_sprite))
				self.main_window.blit(self.item3,self.position_item3)
			else:
				pass

			return self.position_item1,self.position_item2,self.position_item3
			pygame.display.flip()
				




	def load_inventory(self):

		self.inventory = pygame.font.SysFont("monospace", 20)
		self.inventory_display = self.inventory.render("Number of artefacts : 0/3", 1, (255,255,0))
		self.main_window.blit(self.inventory_display, inventory_display_position)	



			
	def share_position(self,player_position):

		if player_position == self.position_item1 :
			self.item_inventory.append(1)
			self.position_item1 = False
			self.catch_item1 = True
			return self.position_item1			
			return self.catch_item1
		
		if player_position == self.position_item2:
			self.item_inventory.append(1)
			self.position_item2 = False
			self.catch_item2 = True
			return self.position_item2			
			return self.catch_item2

		if player_position == self.position_item3:
			self.item_inventory.append(1)
			self.position_item3 = False
			self.catch_item3 = True
			return self.position_item3			
			return self.catch_item3
	
	
	def refresh_load_inventory(self):

		if len(self.item_inventory) == 0:
			self.inventory = pygame.font.SysFont("monospace", 20)
			self.inventory_display = self.inventory.render("Number of artefacts : 0/3", 1, (255,255,0))
			self.main_window.blit(self.inventory_display, inventory_display_position)				

		if len(self.item_inventory) == 1:
			self.inventory = pygame.font.SysFont("monospace", 20)
			self.inventory_display = self.inventory.render("Number of artefacts : 1/3", 1, (255,255,0))
			self.main_window.blit(self.inventory_display, inventory_display_position)	

		elif len(self.item_inventory) == 2:
			self.inventory = pygame.font.SysFont("monospace", 20)
			self.inventory_display = self.inventory.render("Number of artefacts : 2/3", 1, (255,255,0))
			self.main_window.blit(self.inventory_display, inventory_display_position)	

		elif len(self.item_inventory) == 3:
			self.inventory = pygame.font.SysFont("monospace", 20)
			self.inventory_display = self.inventory.render("Number of artefacts : 3/3", 1, (255,255,0))
			self.main_window.blit(self.inventory_display, inventory_display_position)	

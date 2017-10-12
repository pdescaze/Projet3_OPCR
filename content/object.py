""" Module for the class Object"""
#!/usr/bin/python3
# -*- coding: Utf-8 -*

import json
import pygame
from pygame.locals import *
from random import randint
from content.constants import *

class Object():
	"""Class that permits to generate and load 3 differents objects at a
	random position. These 3 objects spawn to a different position.
	This class contains methods for the inventory (load and refresh) and
	a method "share_position" that permits to test if the position of the
	hero is the same as the position of one of the objects"""
	def __init__(self, artwork, object3, file, main_window):
		self.file = file
		#Initialization of pictures
		self.artwork = artwork#object1 and object2
		self.object3 = object3
		self.main_window = main_window
		#Initialization of a loop to generate 3 differents position
		self.proceed = 1
		#Initialization of tests and inventory
		self.test_item1, self.test_item2, self.test_item3 = False, False, False
		self.item_inventory = []
		self.catch_item1, self.catch_item2, self.catch_item3 = False, False, False

	def generate(self):
		""" This method permits to generate 3 random different position
		for the objects. These positions can only be on field sprite"""
		structure = json.load(open(self.file))

		while self.proceed:
			#Line_number equals the line of the first object/item
			#Sprite number equals the sprite in the line
			self.line_number = randint(0, len(structure) - 1)
			self.sprite_number = randint(0, SPRITE_PER_SIDE - 1)
			#Line_number equals the line of the second object/item
			#Sprite number equals the sprite in the line
			self.line_number2 = randint(0, len(structure) - 1)
			self.sprite_number2 = randint(0, SPRITE_PER_SIDE - 1)
			#Line_number equals the line of the third object/item
			#Sprite number equals the sprite in the line
			self.line_number3 = randint(0, len(structure) - 1)
			self.sprite_number3 = randint(0, SPRITE_PER_SIDE - 1)
			#Test if the line and the sprite randomly generate for the first
			#object is not on a field sprite
			if structure[self.line_number][self.sprite_number] != "O":
				self.test_item1 = False
			else:
				self.test_item1 = True

			if self.line_number2 != self.line_number or self.line_number2 == self.line_number \
			and self.sprite_number2 != self.sprite_number:
				if structure[self.line_number2][self.sprite_number2] != "O":
					self.test_item2 = False
				else:
					self.test_item2 = True
			else:
				self.test_item2 = False

			if self.line_number3 != self.line_number and self.line_number3 != self.line_number2 \
			or self.line_number3 == self.line_number and self.sprite_number3 != self.sprite_number \
			or self.line_number3 == self.line_number2 and self.sprite_number3 != self.sprite_number2:
				if structure[self.line_number3][self.sprite_number3] != "O":
					self.test_item3 = False
				else:
					self.test_item3 = True
			else:
				self.test_item3 = False

			if self.test_item1 == True and self.test_item2 == True and self.test_item3 == True:
				self.proceed = 0
			else:
				self.proceed = 1

	def loading(self):
		""" Method that permits to load the picture of objects at their randomly
		generate position if the test_item is True"""
		if self.test_item1 == True:
			self.pick_item1 = pygame.image.load(self.artwork).convert_alpha()
			self.item1 = self.pick_item1.subsurface(ARTWORK_OBJECT1)
			self.item1 = pygame.transform.scale(self.item1, \
				(OBJECT_SPRITE_SIZE, OBJECT_SPRITE_SIZE))
			self.position_item1 = self.item1.get_rect(center=(self.sprite_number * SPRITE_SIZE \
				+ HALF_SPRITE, self.line_number * SPRITE_SIZE + HALF_SPRITE))
			self.main_window.blit(self.item1, self.position_item1)
		else:
			pass

		if self.test_item2 == True:
			self.pick_item2 = pygame.image.load(self.artwork).convert_alpha()
			self.item2 = self.pick_item2.subsurface(ARTWORK_OBJECT2)
			self.item2 = pygame.transform.scale(self.item2, \
				(OBJECT_SPRITE_SIZE, OBJECT_SPRITE_SIZE))
			self.position_item2 = self.item2.get_rect(center=(self.sprite_number2 * SPRITE_SIZE \
				+ HALF_SPRITE, self.line_number2 * SPRITE_SIZE + HALF_SPRITE))
			self.main_window.blit(self.item2, self.position_item2)
		else:
			pass

		if self.test_item3 == True:
			self.item3 = pygame.image.load(self.object3).convert_alpha()
			self.item3 = pygame.transform.scale(self.item3, \
				(OBJECT_SPRITE_SIZE, OBJECT_SPRITE_SIZE))
			self.position_item3 = self.item3.get_rect(center=(self.sprite_number3 * SPRITE_SIZE \
				+ HALF_SPRITE, self.line_number3 * SPRITE_SIZE + HALF_SPRITE))
			self.main_window.blit(self.item3, self.position_item3)
		else:
			pass

		return self.position_item1, self.position_item2, self.position_item3

	def load_inventory(self):
		""" Method that permits to load the inventory in the
		adjacent frame and to initializate it at 0"""
		self.inventory = pygame.font.SysFont("monospace", 20)
		self.inventory_display = self.inventory.render("Number of artefacts : 0/3", \
			1, (255, 255, 0))
		self.main_window.blit(self.inventory_display, INVENTORY_DISPLAY_POSITION)

	def refresh_load_inventory(self):
		"""Method that permits to refresh the inventory in the
		adjacent frame if objects have been caught by the hero"""
		if len(self.item_inventory) == 0:
			self.inventory = pygame.font.SysFont("monospace", 20)
			self.inventory_display = self.inventory.render("Number of artefacts : 0/3", \
				1, (255, 255, 0))
			self.main_window.blit(self.inventory_display, INVENTORY_DISPLAY_POSITION)

		if len(self.item_inventory) == 1:
			self.inventory = pygame.font.SysFont("monospace", 20)
			self.inventory_display = self.inventory.render("Number of artefacts : 1/3", \
				1, (255, 255, 0))
			self.main_window.blit(self.inventory_display, INVENTORY_DISPLAY_POSITION)

		elif len(self.item_inventory) == 2:
			self.inventory = pygame.font.SysFont("monospace", 20)
			self.inventory_display = self.inventory.render("Number of artefacts : 2/3", \
				1, (255, 255, 0))
			self.main_window.blit(self.inventory_display, INVENTORY_DISPLAY_POSITION)

		elif len(self.item_inventory) == 3:
			self.inventory = pygame.font.SysFont("monospace", 20)
			self.inventory_display = self.inventory.render("Number of artefacts : 3/3", \
				1, (255, 255, 0))
			self.main_window.blit(self.inventory_display, INVENTORY_DISPLAY_POSITION)

	def share_position(self, player_position):
		""" Method that permits to test collision between objects
		and the hero. If the hero position is the same as one of the
		object position, the inventory is updated"""
		if player_position == self.position_item1:
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
	
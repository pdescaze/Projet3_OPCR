#!/usr/bin/python3
# -*- coding: Utf-8 -*


""" Labyrinth within Mcgyver has to find and pick up 3 objects around the map
 in order to defeat the guardian and leave the labyrinth.
w = wall; a = arrival; O = field; s=start"""



import os
import sys
import json
import pygame
from pygame.locals import *

from content.constants import *
from content.hero import Character
from content.object import Object
from content.opponent import Opponent
from content.structure import Structure


pygame.init()

main_window= pygame.display.set_mode((window_side_x,window_side_y))
pygame.display.set_caption("McGyver escape")
proceed_main=True

while proceed_main == True:

	""" Initialization of objects"""
	Labyrinth=Structure("labyrinth.json",main_window)
	Mcgyver=Character("pictures/Mcgyver.png","labyrinth.json",main_window)
	Objects=Object("pictures/artwork.png","pictures/needle.png",
		"labyrinth.json",main_window)
	Guardian=Opponent("pictures/guardian.png","labyrinth.json",main_window)

	""" Loading of structure, inventory, hero, objects and guardian"""
	Objects.generate()
	Labyrinth.loading()
	Labyrinth.load_frame()
	Objects.loading()
	Mcgyver.loading()	
	Guardian.loading()
	Objects.load_inventory()
	pygame.display.flip()	

	proceed_game=True


	for event in pygame.event.get():
		if event.type == QUIT:
			proceed_main =False	
			proceed_game=False		

		elif event.type == KEYUP:
			if event.key == K_ESCAPE:
				proceed_main =False
				proceed_game=False		

			
	while proceed_game == True :
		"""Loop of each movement realised by Mcgyver and consequences"""
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			if event.type == QUIT:
				proceed_game=False
				proceed_main=False

			elif event.type == KEYUP:
				if event.key == K_ESCAPE:
					proceed_game=False
					proceed_main=False	
				elif event.key == K_UP:
					Mcgyver.movement("up")
				elif event.key == K_DOWN:
					Mcgyver.movement("down")
				elif event.key == K_RIGHT:
					Mcgyver.movement("right")
				elif event.key == K_LEFT:
					Mcgyver.movement("left")	

		"""After each movement, the collision between the hero and objects are tested
		and the inventory is refresh. The collision between the hero and the guardian
		are also tested"""
		main_window.blit(Mcgyver.player,Mcgyver.position_player)
		Objects.share_position(Mcgyver.position_player)
		Objects.refresh_load_inventory()
		Labyrinth.test_position(Mcgyver.position_player,Guardian.position_guardian,
			Objects.catch_item1,Objects.catch_item2,Objects.catch_item3)		

		if Labyrinth.status == 1:
			Labyrinth.load_defeat("pictures/defeat.png","pictures/artwork.png")
			proceed_game=False	
		elif Labyrinth.status == 2:
			Labyrinth.load_victory("pictures/victory.png")
			proceed_game=False			
		else:
			pass

		pygame.display.flip()
		





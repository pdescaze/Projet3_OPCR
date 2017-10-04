#!/usr/bin/python3
# -*- coding: Utf-8 -*

""" Labyrinth within Mcgyver has to find and pick up 3 objects around the map
 in order to defeat the guardian and leave the labyrinth.
w = wall; a = arrival; O = field; s=start"""

import pygame
from pygame.locals import *

from content.constants import WINDOW_SIDE_X, WINDOW_SIDE_Y
from content.hero import Character
from content.object import Object
from content.opponent import Opponent
from content.structure import Structure


pygame.init()

main_window = pygame.display.set_mode((WINDOW_SIDE_X, WINDOW_SIDE_Y))
pygame.display.set_caption("McGyver escape")
PROCEED_MAIN = 1

while PROCEED_MAIN:

	pygame.time.Clock().tick()

	#Initialization of objects
	labyrinth = Structure("labyrinth.json", main_window)
	mcgyver = Character("pictures/Mcgyver.png", "labyrinth.json", main_window)
	objects = Object("pictures/artwork.png", "pictures/needle.png", "labyrinth.json", main_window)
	guardian = Opponent("pictures/guardian.png", "labyrinth.json", main_window)

	#Loading of structure, inventory, hero, objects and guardian
	objects.generate()
	labyrinth.loading()
	labyrinth.load_frame()
	objects.loading()
	mcgyver.loading()
	guardian.loading()
	objects.load_inventory()
	labyrinth.advices_quit()
	labyrinth.advices_play()
	pygame.display.flip()

	PROCEED_GAME = 1


	for event in pygame.event.get():
		if event.type == QUIT:
			PROCEED_MAIN = 0
			PROCEED_GAME = 0
		elif event.type == KEYUP:
			if event.key == K_ESCAPE:
				PROCEED_MAIN = 0
				PROCEED_GAME = 0

	while PROCEED_GAME:
		#Loop of each movement realised by Mcgyver and consequences
		pygame.time.Clock().tick()

		for event in pygame.event.get():
			if event.type == QUIT:
				PROCEED_GAME = 0
				PROCEED_MAIN = 0
			elif event.type == KEYUP:
				if event.key == K_ESCAPE:
					PROCEED_GAME = 0
					PROCEED_MAIN = 0
				elif event.key == K_UP:
					mcgyver.movement("up")
				elif event.key == K_DOWN:
					mcgyver.movement("down")
				elif event.key == K_RIGHT:
					mcgyver.movement("right")
				elif event.key == K_LEFT:
					mcgyver.movement("left")

		#After each movement, the collision between the hero and objects are tested
		#and the inventory is refresh. The collision between the hero and the guardian
		#are also tested
		main_window.blit(mcgyver.player, mcgyver.position_player)
		objects.share_position(mcgyver.position_player)
		objects.refresh_load_inventory()
		labyrinth.test_position(mcgyver.position_player, guardian.position_guardian, \
			objects.catch_item1, objects.catch_item2, objects.catch_item3)

		if labyrinth.status == 1:
			labyrinth.load_defeat("pictures/defeat.png", "pictures/artwork.png")
			PROCEED_GAME = 0
		elif labyrinth.status == 2:
			labyrinth.load_victory("pictures/victory.png")
			PROCEED_GAME = 0
		else:
			pass
		pygame.display.flip()
		
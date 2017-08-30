#!/usr/bin/python3
# -*- coding: Utf-8 -*


""" Labyrinth within Mcgyver has to find and pick up 3 objects around the map in order to defeat the guardian and leave the labyrinth.
w = wall; a = arrival; O = field; s=start"""



import os
import sys
import json
import pygame
from pygame.locals import *

from constants import *
from classes import *



pygame.init()

main_window= pygame.display.set_mode((window_side,window_side))

proceed=1
while proceed:

	pygame.time.Clock().tick(30)

	Labyrinth=Structure("labyrinthe.json")
	Labyrinth.loading(main_window)
	pygame.display.flip()

	Mcgyver=Character("Mcgyver.png","labyrinthe.json")
	Mcgyver.loading(main_window)
	Guardian=Opponent("guardian.png","labyrinthe.json")
	Guardian.loading(main_window)
	proceed_game=1
	
	for event in pygame.event.get():

			if event.type == QUIT:
				proceed=0
				proceed_game=0


	while proceed_game:
	
		for event in pygame.event.get():

			if event.type == QUIT:
				proceed=0
				proceed_game=0

			elif event.type == KEYUP:
				if event.key == K_UP:
					Mcgyver.movement("up")
				if event.key == K_DOWN:
					Mcgyver.movement("down")
				if event.key == K_RIGHT:
					Mcgyver.movement("right")
				if event.key == K_LEFT:
					Mcgyver.movement("left")

			main_window.blit(Mcgyver.player,Mcgyver.position_player)
			pygame.display.flip()